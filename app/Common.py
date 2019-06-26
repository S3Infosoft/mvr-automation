from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from local import Booking
from local import Goibibo
from ddl_sql import Database
import datetime


def main():
    name = input("Select agent :\n booking.com \t goibibo.com\n")
    month, year = input("Enter Month and Year (eg. May 2019):\t").split(" ")
    cin, cout = input("Enter check-in and check-out dates (eg. 20 22):\t").split(" ")
    print(run(name, month, year, cin, cout))


def month_converter(mnth):
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
              'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    return "%02d" % (months.index(mnth.lower()[:3])+1)

def run(name, month, year, cin, cout):
    agent_name = ["booking.com", "goibibo.com"]
    x = None
    if name == agent_name[0]:
        x = 0
    elif name == agent_name[1]:
        x = 1
    agent = [Booking(), Goibibo()]
    datein = year+"-"+month_converter(month)+"-"+str("%02d" % int(cin))
    dateout = year+"-"+month_converter(month)+"-"+str("%02d" % int(cout))
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--window-size=1420,1080')
    options.add_argument('--disable-gpu')

    # driver = webdriver.Chrome(chrome_options=options,
    #                           executable_path=r'chromedriver.exe')
    driver = webdriver.Remote(
              command_executor='http://selenium-hub:4444/wd/hub',
              desired_capabilities=DesiredCapabilities.CHROME)

    driver.set_page_load_timeout(15)
    driver.maximize_window()
    driver.get(agent[x].target)
    driver.find_element_by_css_selector(agent[x].calender).click()
    flag1 = True
    flag2 = True
    weekin = str(0)
    weekout = str(0)
    for i in range(6):
        temp = driver.find_element_by_xpath(agent[x].week_finder+str(i+1)+"]").text.split(" ")
        if any(cin in s for s in temp) and flag1:
            weekin = str(i+1)
            flag1 = False
        if any(cout in s for s in temp) and flag2:
            weekout = str(i+1)
            flag2 = False
    dayin = [datein, cin]
    dayout = [dateout, cout]
    driver.find_element_by_xpath(agent[x].day_in(weekin, dayin[x])).click()
    driver.find_element_by_xpath(agent[x].day_out(weekout, dayout[x])).click()
    driver.find_element_by_id(agent[x].search_id).send_keys(agent[x].search_key)
    time.sleep(1)
    waiting = WebDriverWait(driver, 10)
    waiting.until(ec.visibility_of_element_located((By.ID, agent[x].search_id)))\
        .send_keys(Keys.ARROW_DOWN+Keys.ENTER+Keys.ENTER)
    listed = agent[x].listing(driver)
    agent[x].hotel_find(driver)
    driver.switch_to.window(driver.window_handles[1])
    driver.quit()
    time.sleep(3)
    data = agent[x].data_scraping(driver)
    time.sleep(1)
    current_time = datetime.datetime.now()
    time1 = current_time.strftime("%Y-%m-%d %H:%M:%S")
    sql = Database()
    # sql.create_table()
    sql.insert_table(time1, agent_name[x], datein, dateout, listed,
                     str(data[0]), str(data[1]), str(data[2]), str(data[3]))
    # sql.print_db()
    return time1, agent_name[x], datein, dateout, listed, str(data[0]), str(data[1]), str(data[2]), str(data[3])


if __name__ == "__main__":
    main()
