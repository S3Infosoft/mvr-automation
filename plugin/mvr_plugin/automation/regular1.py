from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from .local1 import *
import requests
# from Common import main_run
# from ddl_sql import Database
import datetime

S = "room_type_id_421644301"

def month_select(driver,din):
    cindate,month,year=din.split('/')
    cindate=int(cindate)
    year=int(year)
    month=int(month)
    print(cindate,month,year)
    dt=datetime.datetime.today()
    cur_month=dt.month
    cur_year=dt.year
    if month==cur_month and year==cur_year:
        print('m=cm and yr=cr')
    else:
        if month-cur_month>0:
            if cur_year==year:
                mon_diff=(month-cur_month)

                for i in range(mon_diff):
                    driver.find_element_by_xpath('//*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[2]').click()
                print('m-cm>0 and cy==yr')

                return mon_diff
            elif cur_year>year:
                print('Invalid dates')
                exit(0)
            elif cur_year<year:

                no_of_click = 12 * (year - cur_year)+(month - cur_month)
                for i in range(no_of_click):
                    driver.find_element_by_xpath('//*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[2]/svg').click()

                print('m-cm>0 and cy<yr')
                return no_of_click

        elif month<cur_month:
            if year<=cur_year:
                print("You cant checkin before today")
                exit(0)
            elif year>cur_year:
                no_of_click=12*(year-cur_year)-(cur_month-month)

                for i in range(no_of_click):
                    driver.find_element_by_xpath('//*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[2]/svg').click()
                print('m<cm and cy<yr')
                return no_of_click



def main():
    agent = Booking()
    search_text = "Ratnagiri"
    hotel_name = "Mango Valley Resort Ganpatipule"
    hotel_id = "4216443"
    checkin = "30/03/2019"
    checkout = "31/03/2019"
    room_typeids = ["room_type_id_421644306", "room_type_id_421644302",
                    "room_type_id_421644305", "room_type_id_421644303"]
    room_priceids = ["421644306_174652031_0_42_0",
                     "421644302_141698786_0_42_0", "421644302_174652031_0_42_0",
                     "421644305_174652031_0_42_0", "421644303_174652031_0_42_0"]
    room_ids = ["roomrtc_45000574650", "roomrtc_45000574663", "roomrtc_45000653101", "roomrtc_45000574667"]
    print(main_run(agent, hotel_id, search_text, checkin, checkout,
                   room_typeids=room_typeids, room_priceids=room_priceids))


# def calender_ctrl(agent, cin, cout,driver):
#     driver.find_element_by_css_selector(agent.calender).click()
#     print('a')
#     # month_select(driver,din)
#     print('b')
#     cin = str("%01d" % int(cin))
#     cout = str("%01d" % int(cout))
#     flag1 = True
#     flag2 = True
#     weekin = str(0)
#     weekout = str(0)
#     for i in range(7):
#         temp = driver.find_element_by_xpath(agent.week_finder+str(i+1)+"]").text.split(" ")
#         print(temp)
#         if any(cin in s for s in temp) and flag1:
#             weekin = str(i+1)
#             flag1 = False
#         if any(cout in s for s in temp) and flag2:
#             weekout = str(i+1)
#             return weekin, weekout

def calender_ctrl_new(agent, cin, cout,driver,din,dout,datein,dateout):
    driver.find_element_by_css_selector(agent.calender).click()
    print('a')
    cin = str("%01d" % int(cin))
    no_of_click=month_select(driver,din)
    flag1 = True
    weekin = str(0)
    print('b')
    for i in range(7):
        temp = driver.find_element_by_xpath(agent.week_finder + str(i + 1) + "]").text.split(" ")
        print(temp)
        if any(cin in s for s in temp) and flag1:
            weekin = str(i + 1)
            flag1 = False
            driver.find_element_by_xpath(agent.day_in(weekin,datein)).click()
            break
    # now returning to current month
    try:
         for i in range(no_of_click):
             driver.find_element_by_xpath('// *[ @ id = "frm"] / div[1] / div[2] / div[2] / div / div / div[1]').click()
    except Exception as e:
         print(e,e.args)
         pass
    print('c')
    month_select(driver, dout)
    time.sleep(1)
    print('d')
    cout = str("%01d" % int(cout))
    flag2 = True
    weekout=str(0)
    for i in range(7):
        temp = driver.find_element_by_xpath(agent.week_finder + str(i + 1) + "]").text.split(" ")
        print(temp)
        if any(cout in s for s in temp) and flag2:
                weekout = str(i + 1)
                driver.find_element_by_xpath(agent.day_out(weekout,dateout)).click()
                return weekin, weekout




class MasterMMT(object):
    @staticmethod
    def run(search_text, hotel_id, hotel_name, din, dout, room_id):
        current_time = datetime.datetime.now()
        time1 = current_time.strftime("%Y-%m-%d %H:%M:%S")
        # print(f"current time is {current_time} \n time1={time1}")
        agent = Mmt()
        agent_name = agent.__class__.__name__

        driver = start_driver()
        listed = agent.listing(driver, hotel_id, search_text, din, dout)
        if int(listed)==0:
            returndata = sql_entry('not found', agent_name, din, dout, f'{hotel_name} not found', time1,hotel_name)
            driver.quit()
            return returndata


        driver = start_driver()
        agent.hotel_find(driver, hotel_id, hotel_name, din, dout)
        data = agent.data_scraping(driver, room_id)
        print(data)
        driver.quit()
        returndata = sql_entry(listed, agent_name, din, dout, data, time1)
        return returndata


def start_driver(clint):
    global driver
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--window-size=1420,1080')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("enable-automation");
    options.add_argument("--disable-extensions");
    options.add_argument("--dns-prefetch-disable");
    options.add_argument("--disable-gpu");

    # nodeurl = 'http://192.168.99.100:4445/wd/hub'
    nodeurl = clint
    # driver = webdriver.Chrome(chrome_options=options, executable_path=r'chromedriver.exe')
    # url = driver.command_executor._url
    caps = DesiredCapabilities.CHROME.copy()
    # caps['max_duration'] = 100

    print(caps)
    driver = webdriver.Remote(
        command_executor=nodeurl,
        # desired_capabilities=DesiredCapabilities.CHROME)
        desired_capabilities=caps)
    driver.set_page_load_timeout(500)
    driver.implicitly_wait(10)
    driver.maximize_window()


    return driver


def sql_entry(listed, agent_name, din, dout, data, time1,hotel_name):
    current_time = datetime.datetime.now()
    time2 = current_time.strftime("%Y-%m-%d %H:%M:%S")
    # sql = Database()
    # sql.create_table()
    # sql.insert_table(time1, agent_name, din, dout, listed,
    #                  str(data[0]), str(data[1]), str(data[2]), str(data[3]))
    # sql.print_db()
    returndata = {}
    returndata['start_time'] = time1
    returndata['end_time'] = time2
    returndata['ota'] = agent_name
    returndata['check_in'] = din
    returndata['check_out'] = dout
    returndata['listed_position'] = listed
    # returndata['Std_EP'] = str(data[0])
    # returndata['Std_CP'] = str(data[1])
    # returndata['Sup_EP'] = str(data[2])
    # returndata['Sup_CP'] = str(data[3])
    i = 0
    rates = {}
    if type(data)==str:
        returndata['rates'] = data
        returndata['Status'] = 'NOT OK'
        return returndata

    while i < len(data):
        rates[data[i]] = str(data[i+1])
        i = i+2
    returndata['rates'] = rates
    returndata['Status'] = 'OK'
    returndata['hotel_name']=hotel_name
    return returndata


def main_run(agent, hotel_prop, search_text, din, dout,hotel_name,clint, **kwargs):
    current_time = datetime.datetime.now()
    time1 = current_time.strftime("%Y-%m-%d %H:%M:%S")
    driver = start_driver(clint)
    driver.maximize_window()
    agent_name = agent.__class__.__name__
    driver.get(agent.target)
    cin, month, year = din.split("/")
    cout, month_out, year_out = dout.split("/")
    datein = year+"-"+month+"-"+cin
    dateout = year_out+"-"+month_out+"-"+cout
    print(datein,dateout)

    try:
        weekin, weekout = calender_ctrl_new(agent, cin, cout,driver,din,dout,datein,dateout)
    except Exception as e:
        print(e.args,e)

        return driver
    # month_select(driver,din)

    # driver.find_element_by_xpath(agent.day_in(weekin, datein)).click()
    # month_select(driver,dout)
    # driver.find_element_by_xpath(agent.day_out(weekout, dateout)).click()
    driver.find_element_by_id(agent.search_id).send_keys(search_text+Keys.ENTER)
    time.sleep(1)
    agent.proceed(driver)
    listed = agent.listing(driver, hotel_prop)
    # print('a')
    if int(listed)==0:
        returndata=sql_entry('Not found',agent_name,din,dout,f'{hotel_prop} not found',time1,hotel_name)
        driver.quit()
        return returndata
    # print('b')
    agent.hotel_find(driver, hotel_prop)
    driver.switch_to.window(driver.window_handles[1])

    print('ab')
    time.sleep(5)
    # driver.find_element_by_tag_name("body").send_keys("Keys.ESCAPE");
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    data = agent.data_scraping(driver, **kwargs)
    time.sleep(1)
    driver.quit()
    returndata = sql_entry(listed, agent_name, din, dout, data, time1,hotel_name)
    return returndata

def main_run_for_new_goibibo(driver,agent, hotel_prop, search_text, din, dout,hotel_name, **kwargs):
    current_time = datetime.datetime.now()
    time1 = current_time.strftime("%Y-%m-%d %H:%M:%S")
    # driver = start_driver()
    # agent_name = agent.__class__.__name__
    # driver.get(agent.target)
    agent=NewGoibibo()
    driver.maximize_window()
    agent_name = agent.__class__.__name__
    cin, month, year = din.split("/")
    cout, month, year = dout.split("/")
    datein = year+"-"+month+"-"+cin
    dateout = year+"-"+month+"-"+cout

    driver.find_element_by_xpath('//*[@id="root"]/section/div/div[3]/section[1]/div[1]/div/div[3]/div/div[1]').click()
    driver.find_element_by_xpath(agent.day_in(driver,datein)).click()
    # time.sleep(5)

    driver.find_element_by_xpath(agent.day_out(driver, dateout)).click()

    driver.find_element_by_id(agent.search_id).send_keys(search_text+Keys.ENTER)
    time.sleep(1)
    agent.proceed(driver)
    listed = agent.listing(driver, hotel_prop)
    if int(listed)==0:
        print('a')
        returndata=sql_entry('Not found',agent_name,din,dout,f'{hotel_prop} not found',time1,hotel_name)
        driver.quit()
        return returndata
    print('b')
    agent.hotel_find(driver, hotel_prop,int(listed))
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    data = agent.data_scraping(driver)
    time.sleep(1)
    driver.quit()
    returndata = sql_entry(listed, agent_name, din, dout, data, time1,hotel_name)
    return returndata

# return True if element is visible within 30 seconds, otherwise False


if __name__ == "__main__":
    main()
