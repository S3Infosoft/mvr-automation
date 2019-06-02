from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from local import booking
from local import goibibo
import sqlite3

def month_converter(month):
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    return "%02d"%(months.index(month.lower()[:3])+1)

agent=[booking,goibibo]
x=int(input("Select agent :\n 0 for booking.com \t 1 for goibibo.com\n"))
month,year=input("Enter Month and Year (eg. May 2019):\t").split(" ")
cin,cout=input("Enter check-in and check-out dates (eg. 20 22):\t").split(" ")
datein=year+"-"+month_converter(month)+"-"+str("%02d"%int(cin))
dateout=year+"-"+month_converter(month)+"-"+str("%02d"%int(cout))
driver=webdriver.Chrome(r"C:\Users\91845\PycharmProjects\RPA_MVR\Driver\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.maximize_window()
driver.get(agent[x].target)
driver.find_element_by_css_selector(agent[x].calender).click()
flag1=True
flag2=True
for i in range(6):
    temp=(driver.find_element_by_xpath(agent[x].week_finder+str(i+1)+"]").text).split(" ")
    if any(cin in s for s in temp) and flag1:
        weekin=str(i+1)
        flag1=False
    if any(cout in s for s in temp) and flag2:
        weekout=str(i+1)
        flag2=False
dayin=[datein,cin]
dayout=[dateout,cout]
driver.find_element_by_xpath(agent[x].day_in(weekin,dayin[x])).click()
driver.find_element_by_xpath(agent[x].day_out(weekout,dayout[x])).click()
driver.find_element_by_id(agent[x].search_id).send_keys(agent[x].search_key)
time.sleep(1)
waiting=WebDriverWait(driver,10)
waiting.until(EC.visibility_of_element_located((By.ID, agent[x].search_id))).send_keys(Keys.ARROW_DOWN+Keys.ENTER+Keys.ENTER)
listed=agent[x].listing(driver)
agent[x].hotel_find(driver)
driver.switch_to_window(driver.window_handles[1])
time.sleep(2)
data=agent[x].datascraping(driver)
conn=sqlite3.connect('Data.db')
c=conn.cursor()
c.execute("INSERT INTO Data VALUES(?,?,?,?,?,?,?,?)",(str(agent[x]),datein,dateout,listed,str(data[0]),str(data[1]),str(data[2]),str(data[3])))
conn.commit()
c.execute("SELECT * FROM Data")
rows=c.fetchall()
for row in rows:
    print(row)
conn.close()
