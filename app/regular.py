from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from local import *
# from Common import main_run
from ddl_sql import Database
import datetime


def main():
    agent = Goibibo()
    search_text = "Ganpatipule"
    hotel_name = "Mango Valley Resort Ganpatipule"
    checkin = "06/07/2019"
    checkout = "07/07/2019"
    try:
        print(main_run(agent, hotel_name, search_text, checkin, checkout))
        # return main_run(agent,  hotel_name, search_text, checkin, checkout)
    except TimeoutException:
        print("TIMEOUT ERROR")
    pass


def calender_ctrl(agent, cin, cout):
    driver.find_element_by_css_selector(agent.calender).click()
    cin = str("%01d" % int(cin))
    cout = str("%01d" % int(cout))
    flag1 = True
    flag2 = True
    weekin = str(0)
    weekout = str(0)
    for i in range(7):
        temp = driver.find_element_by_xpath(agent.week_finder+str(i+1)+"]").text.split(" ")
        if any(cin in s for s in temp) and flag1:
            weekin = str(i+1)
            flag1 = False
        if any(cout in s for s in temp) and flag2:
            weekout = str(i+1)
            return weekin, weekout


class MasterMMT(object):
    @staticmethod
    def run(search_text, din, dout):
        agent = Mmt()
        agent_name = agent.__class__.__name__
        driver = start_driver()
        listed = agent.listing(driver, search_text, din, dout)
        driver.quit()
        driver = start_driver()
        agent.hotel_find(driver, din, dout)
        data = agent.data_scraping(driver)
        driver.quit()
        returndata = sql_entry(listed, agent_name, din, dout, data)
        return returndata


def start_driver():
    global driver
    options = Options()
    # options.add_argument("--headless")
    options.add_argument('--window-size=1420,1080')
    options.add_argument('--disable-gpu')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=options,
                               executable_path=r'chromedriver.exe')
    # driver = webdriver.Remote(
    #     command_executor='http://selenium-hub:4444/wd/hub',
    #     desired_capabilities=DesiredCapabilities.CHROME)

    driver.set_page_load_timeout(30)
    driver.maximize_window()
    return driver


def sql_entry(listed, agent_name, din, dout, data):
    current_time = datetime.datetime.now()
    time1 = current_time.strftime("%Y-%m-%d %H:%M:%S")
    sql = Database()
    # sql.create_table()
    sql.insert_table(time1, agent_name, din, dout, listed,
                     str(data[0]), str(data[1]), str(data[2]), str(data[3]))
    # sql.print_db()
    returndata = {}
    returndata['run_time'] = time1
    returndata['ota'] = agent_name
    returndata['check_in'] = din
    returndata['check_out'] = dout
    returndata['listed_position'] = listed
    returndata['Std_EP'] = str(data[0])
    returndata['Std_CP'] = str(data[1])
    returndata['Sup_EP'] = str(data[2])
    returndata['Sup_CP'] = str(data[3])
    returndata['Status'] = 'OK'
    return returndata


def main_run(agent, hotel_prop, search_text, din, dout):
    driver = start_driver()
    agent_name = agent.__class__.__name__
    driver.get(agent.target)
    cin, month, year = din.split("/")
    cout, month, year = dout.split("/")
    datein = year+"-"+month+"-"+cin
    dateout = year+"-"+month+"-"+cout
    weekin, weekout = calender_ctrl(agent, cin, cout)
    driver.find_element_by_xpath(agent.day_in(weekin, datein)).click()
    driver.find_element_by_xpath(agent.day_out(weekout, dateout)).click()
    driver.find_element_by_id(agent.search_id).send_keys(search_text+Keys.ENTER)
    time.sleep(1)
    agent.proceed(driver)
    # waiting = WebDriverWait(driver, 10)
    # waiting.until(ec.visibility_of_element_located((By.ID, agent.search_id)))\
    #     .send_keys(Keys.ARROW_DOWN+Keys.ENTER+Keys.ENTER)
    listed = agent.listing(driver, hotel_prop)
    agent.hotel_find(driver, hotel_prop)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    data = agent.data_scraping(driver)
    time.sleep(1)
    driver.quit()
    returndata = sql_entry(listed, agent_name, din, dout, data)
    return returndata


if __name__ == "__main__":
    main()
