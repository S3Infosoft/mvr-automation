import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import json

def month_converter(month):
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    return "%02d"%(months.index(month.lower()[:3])+1)

#month,year=input("Enter Month and Year (eg. May 2019):\t").split(" ")
#cin,cout=input("Enter check-in and check-out dates (eg. 20 22):\t").split(" ")
month,year='June 2019'.split(" ")
cin,cout='20 22'.split(" ")

datein=year+"-"+month_converter(month)+"-"+cin
dateout=year+"-"+month_converter(month)+"-"+cout

if sys.platform == 'darwin':
    driver = webdriver.Chrome()
else:
    driver=webdriver.Chrome(r"C:\Users\91845\PycharmProjects\RPA_MVR\Driver\chromedriver.exe")

driver.set_page_load_timeout(10)
driver.maximize_window()
driver.get("https://www.booking.com/")
driver.find_element_by_name("ss").send_keys("Ratnagiri")
driver.find_element_by_css_selector("span.sb-date-field__icon.sb-date-field__icon-btn.bk-svg-wrapper.calendar-restructure-sb").click()
for i in range(6):
    temp=(driver.find_element_by_xpath("//*[@id='frm']/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr["+str(i+1)+"]").text).split(" ")
    if any(cin in s for s in temp):
        weekin=str(i+1)
    if any(cout in s for s in temp):
        weekout=str(i+1)

driver.find_element_by_xpath("//*[@id='frm']/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr["+weekin+"]/td[@data-date='"+datein+"']").click()
driver.find_element_by_xpath("//*[@id='frm']/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr["+weekout+"]/td[@data-date='"+dateout+"']").click()
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='+'])[3]/following::span[1]").click()
for i in range(20):
    if ((driver.find_element_by_xpath("//*[@id='hotellist_inner']/div[@data-hotelid='4216443']"))== (driver.find_element_by_xpath("//*[@id='hotellist_inner']/div["+str(i+1)+"]"))):
        listing=str("%01d"%((i+1)/2))
driver.find_element_by_xpath("//*[@id='hotellist_inner']/div[@data-hotelid='4216443']/div[2]/div[1]/div[1]/h3/a/span[1]").click()
driver.switch_to_window(driver.window_handles[1])
room_type=[]
EP=[]
CP=[]
try:
    room_type.append(driver.find_element_by_xpath("//*[@id='hprt-form']/table/tbody/tr[1]/td[1]/div/div[1]/a[2]").get_attribute("data-room-name"))
    EP.append(driver.find_element_by_xpath("//form[@id='hprt-form']/table/tbody/tr/td[3]/div/div[2]").text)
except NoSuchElementException:
    pass
try:
    CP.append(driver.find_element_by_xpath("//form[@id='hprt-form']/table/tbody/tr[3]/td[2]/div/div[2]").text)
except NoSuchElementException:
    pass
try:
    room_type.append(driver.find_element_by_xpath("//*[@id='hprt-form']/table/tbody/tr[4]/td[1]/div/div[1]/a[2]").get_attribute("data-room-name"))
    EP.append(driver.find_element_by_xpath("//form[@id='hprt-form']/table/tbody/tr[4]/td[3]/div/div[2]").text)
except NoSuchElementException:
    pass
try:
    CP.append(driver.find_element_by_xpath("//form[@id='hprt-form']/table/tbody/tr[6]/td[2]/div/div[2]").text)
except NoSuchElementException:
    pass

if (len(room_type)>len(CP)):
    for i in range(len(room_type)-len(CP)):
        CP.append("--")
print("Listed position:\t"+listing)
data={"Listed Position":listing }
for i in range(len(room_type)):
    print("Price:\n"+room_type[i]+"\nEP="+EP[i]+"\nCP="+CP[i])
    data.update({"room type":room_type[i], "EP": EP[i],"CP":CP[i]})
with open('data1.json', 'w') as outfile:
    json.dump(data, outfile)