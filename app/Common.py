from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from local import *
# from ddl_sql import Database
import datetime


def main():
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


def start_driver():
    global driver
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--window-size=1420,1080')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Remote(
        command_executor='http://selenium-hub:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)

    driver.set_page_load_timeout(30)
    driver.maximize_window()
    return driver


def sql_entry(listed, agent_name, din, dout, data, time1,hotel_name):
    # sql = Database()
    # sql.create_table()
    # sql.insert_table(time1, agent_name, din, dout, listed,
    #                  str(data[0]), str(data[1]), str(data[2]), str(data[3]))
    # sql.print_db()
    returndata = {}
    current_time = datetime.datetime.now()
    time2 = current_time.strftime("%Y-%m-%d %H:%M:%S")
    returndata['run_start_time'] = time1
    returndata['run_end_time'] = time2
    returndata['ota'] = agent_name
    returndata['check_in'] = din
    returndata['check_out'] = dout
    returndata['listed_position'] = listed
    i = 0
    rates = {}
    while i < len(data):
        rates[data[i]] = str(data[i+1])
        i = i+2
    returndata['rates'] = rates
    returndata['Status'] = 'OK'
    returndata['hotelname']=hotel_name
    return returndata


def main_run(agent, hotel_prop, search_text, din, dout,hotel_name, **kwargs):
    current_time = datetime.datetime.now()
    time1 = current_time.strftime("%Y-%m-%d %H:%M:%S")
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
    listed = agent.listing(driver, hotel_prop)
    agent.hotel_find(driver, hotel_prop)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    data = agent.data_scraping(driver, **kwargs)
    time.sleep(1)
    driver.quit()
    returndata = sql_entry(listed, agent_name, din, dout, data, time1,hotel_name)
    return returndata


if __name__ == "__main__":
    main()
