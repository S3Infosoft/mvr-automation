from selenium.common.exceptions import NoSuchElementException
import  time
from selenium import webdriver

class booking:
    target="https://www.booking.com/"
    search_id="ss"
    search_key="Ratnagiri"
    calender="span.sb-date-field__icon.sb-date-field__icon-btn.bk-svg-wrapper.calendar-restructure-sb"
    week_finder="//*[@id='frm']/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr["
    def day_in(weekin,datein):
        return "//*[@id='frm']/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr["+weekin+"]/td[@data-date='"+datein+"']"
    def day_out(weekout,dateout):
        return "//*[@id='frm']/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr["+weekout+"]/td[@data-date='"+dateout+"']"
    def listing(driver):
        for i in range(20):
            if ((driver.find_element_by_xpath("//*[@id='hotellist_inner']/div[@data-hotelid='4216443']")) == (
            driver.find_element_by_xpath("//*[@id='hotellist_inner']/div[" + str(i + 1) + "]"))):
                listed=str("%01d" % ((i + 1) / 2))
        return listed

    def hotel_find(driver):
        driver.find_element_by_xpath("//*[@id='hotellist_inner']/div[@data-hotelid='4216443']/div[2]/div[1]/div[1]/h3/a/span[1]").click()

    def datascraping(driver):
        Std_EP = "--"
        Std_CP = "--"
        Sup_CP = "--"
        Sup_EP = "--"
        try:
            room_type=driver.find_element_by_xpath("//*[@id='hprt-form']/table/tbody/tr[1]/td[1]/div/div[1]/a[2]").get_attribute("data-room-name")
            if room_type=="Standard Double Room":
                Std_EP=driver.find_element_by_xpath("//form[@id='hprt-form']/table/tbody/tr/td[3]/div/div[2]").text
                Std_CP=driver.find_element_by_xpath("//form[@id='hprt-form']/table/tbody/tr[3]/td[2]/div/div[2]").text
            elif room_type=="Superior Double Room":
                Sup_EP=driver.find_element_by_xpath("//form[@id='hprt-form']/table/tbody/tr/td[3]/div/div[2]").text
                Sup_CP=driver.find_element_by_xpath("//form[@id='hprt-form']/table/tbody/tr[3]/td[2]/div/div[2]").text
        except NoSuchElementException:
            pass
        try:
            room_type = driver.find_element_by_xpath("//*[@id='hprt-form']/table/tbody/tr[4]/td[1]/div/div[1]/a[2]").get_attribute("data-room-name")
            if room_type == "Standard Double Room":
                Std_EP = driver.find_element_by_xpath("//form[@id='hprt-form']/table/tbody/tr[4]/td[3]/div/div[2]").text
                Std_CP = driver.find_element_by_xpath("//form[@id='hprt-form']/table/tbody/tr[5]/td[2]/div/div[2]").text
            elif room_type == "Superior Double Room":
                Sup_EP = driver.find_element_by_xpath("//form[@id='hprt-form']/table/tbody/tr[4]/td[3]/div/div[2]").text
                Sup_CP = driver.find_element_by_xpath("//form[@id='hprt-form']/table/tbody/tr[5]/td[2]/div/div[2]").text
            else:
                if (Std_EP != "--" and Std_CP != "--"):
                    Sup_EP="--"
                    Sup_CP="--"
                elif (Sup_EP != "--" and Sup_CP != "--"):
                    Std_EP="--"
                    Std_CP="--"
        except NoSuchElementException:
            pass
        return Std_EP,Std_CP,Sup_EP,Sup_CP

class goibibo:
    target="https://www.goibibo.com/hotels/"
    search_id="gosuggest_inputL"
    search_key="Ganpatipule"
    calender="input.form-control.inputTxtLarge.widgetCalenderTxt"
    week_finder="//*[@id='Home']/div[3]/div[1]/div/div[1]/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[3]/div["
    def day_in(weekin, cin):
        return "//*[@id='Home']/div[3]/div[1]/div/div[1]/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[3]/div["+weekin+"]/div[text()='"+cin+"']"
    def day_out(weekout,cout):
        return "//*[@id='Home']/div[3]/div[1]/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[2]/div[3]/div["+weekout+"]/div[text()='"+cout+"']"
    def listing(driver):
        i = 0
        while 1:
            Divs = driver.find_element_by_tag_name('div').text
            if 'Mango Valley Resort Ganpatipule' in Divs:
                listed=str("%01d"%(i/ 250))
                driver.execute_script("window.scrollTo(" + str(i) + "," + str(i + 750) + ");")
                time.sleep(1)
                break
            else:
                driver.execute_script("window.scrollTo(" + str(i) + "," + str(i + 250) + ");")
                time.sleep(0.5)
                i = i + 250
                continue
        return listed
    def hotel_find(driver):
        element=driver.find_element_by_link_text("Mango Valley Resort Ganpatipule")
        driver.execute_script("arguments[0].click();", element)
        # for i in range(7):
        #     if ("Mango Valley Resort Ganpatipule" == driver.find_element_by_xpath("//*[@id='srpContainer']/div[2]/div[2]/div/div[2]/div/div[5]/div[1]/div/div/section[" + str(i + 1) + "]/div[2]/div/div[1]/div[1]/div/a/span").text):
        #         driver.find_element_by_xpath("//*[@id='srpContainer']/div[2]/div[2]/div/div[2]/div/div[5]/div[1]/div/div/section[" + str(i + 1) + "]/div[2]/div/div[1]/div[1]/div/a/span").click()
        #         break
        #     else:
        #         continue
    def datascraping(driver):
        try:
            Std_EP=driver.find_element_by_xpath("//*[@id='roomrtc_45000574650']/div/section/section[2]/aside[1]/div[1]/div[3]/div[1]/p[2]/span").text
        except NoSuchElementException:
            Std_EP="--"
            pass
        try:
            Std_CP=driver.find_element_by_xpath("//*[@id='roomrtc_45000574650']/div/section/section[2]/aside[2]/div[1]/div[3]/div[1]/p[2]/span").text
        except NoSuchElementException:
            Std_CP="--"
            pass
        try:
            Sup_EP=driver.find_element_by_xpath("//*[@id='roomrtc_45000574663']/div/section/section[2]/aside[1]/div[1]/div[3]/div[1]/p[2]/span").text
        except NoSuchElementException:
            Sup_EP="--"
            pass
        try:
            Sup_CP=driver.find_element_by_xpath("//*[@id='roomrtc_45000574663']/div/section/section[2]/aside[2]/div[1]/div[3]/div[1]/p[2]/span").text
        except NoSuchElementException:
            Sup_CP="--"
            pass
        return Std_EP,Std_CP,Sup_EP,Std_CP
