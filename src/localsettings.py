from selenium.common.exceptions import NoSuchElementException
import time


class Booking:
    target = "https://www.booking.com/"
    search_id = "ss"
    search_key = "Ratnagiri"
    calender = "span.sb-date-field__icon.sb-date-field__icon-btn.bk-svg-wrapper.calendar-restructure-sb"
    week_finder = "//*[@id='frm']/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr["
    
    def day_in(self, weekin, datein):
        return "//*[@id='frm']/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr["\
               + weekin + "]/td[@data-date='" + datein + "']"
    
    def day_out(self, weekout, dateout):
        return "//*[@id='frm']/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr["\
               + weekout + "]/td[@data-date='" + dateout + "']"
    
    def listing(self, driver):
        for i in range(20):
            if ((driver.find_element_by_xpath("//*[@id='hotellist_inner']/div[@data-hotelid='4216443']")) == (
                 driver.find_element_by_xpath("//*[@id='hotellist_inner']/div[" + str(i + 1) + "]"))):
                listed = str("%01d" % ((i + 1) / 2))
                break
            else:
                listed = str(0)
        return listed

    def hotel_find(self, driver):
        driver.find_element_by_xpath("//*[@id='hotellist_inner']/div[@data-hotelid='4216443']/div[2]/div[1]"
                                     "/div[1]/h3/a/span[1]").click()

    def data_scraping(self, driver):
        std_ep = "--"
        std_cp = "--"
        sup_cp = "--"
        sup_ep = "--"
        try:
            room_type = driver.find_element_by_xpath("//*[@id='hprt-form']/table/tbody/tr[1]/td[1]/div/div[1]/a[2]")\
                .get_attribute("data-room-name")
            if room_type == "Standard Double Room":
                std_ep = driver.find_element_by_xpath("//form[@id='hprt-form']/table/tbody/tr/td[3]/div/div[2]").text
                std_cp = driver.find_element_by_xpath("//form[@id='hprt-form']/table/tbody/tr[3]/td[2]/div/div[2]").text
            elif room_type == "Superior Double Room":
                sup_ep = driver.find_element_by_xpath("//form[@id='hprt-form']/table/tbody/tr/td[3]/div/div[2]").text
                sup_cp = driver.find_element_by_xpath("//form[@id='hprt-form']/table/tbody/tr[3]/td[2]/div/div[2]").text
        except NoSuchElementException:
            pass
        try:
            room_type = driver.find_element_by_xpath("//*[@id='hprt-form']/table/tbody/tr[4]/td[1]/div/div[1]/a[2]")\
                .get_attribute("data-room-name")
            if room_type == "Standard Double Room":
                std_ep = driver.find_element_by_xpath("//form[@id='hprt-form']/table/tbody/tr[4]/td[3]/div/div[2]").text
                std_cp = driver.find_element_by_xpath("//form[@id='hprt-form']/table/tbody/tr[5]/td[2]/div/div[2]").text
            elif room_type == "Superior Double Room":
                sup_ep = driver.find_element_by_xpath("//form[@id='hprt-form']/table/tbody/tr[4]/td[3]/div/div[2]").text
                sup_cp = driver.find_element_by_xpath("//form[@id='hprt-form']/table/tbody/tr[5]/td[2]/div/div[2]").text
            else:
                if std_ep != "--" and std_cp != "--":
                    sup_ep = "--"
                    sup_cp = "--"
                elif sup_ep != "--" and sup_cp != "--":
                    std_ep = "--"
                    std_cp = "--"
        except NoSuchElementException:
            pass
        return std_ep, std_cp, sup_ep, sup_cp


class Goibibo:
    target = "https://www.goibibo.com/hotels/"
    search_id = "gosuggest_inputL"
    search_key = "Ganpatipule"
    calender = "input.form-control.inputTxtLarge.widgetCalenderTxt"
    week_finder = "//*[@id='Home']/div[3]/div[1]/div/div[1]/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[3]/div["
    
    def day_in(self, weekin, cin):
        return "//*[@id='Home']/div[3]/div[1]/div/div[1]/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[3]/div["\
               + weekin + "]/div[text()='" + cin + "']"
    
    def day_out(self, weekout, cout):
        return "//*[@id='Home']/div[3]/div[1]/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[2]/div[3]/div["\
               + weekout + "]/div[text()='" + cout + "']"
    
    def listing(self, driver):
        i = 0
        listed = 0
        for i in range(3):
            try:
                if ("Mango Valley Resort Ganpatipule" == driver.find_element_by_xpath(
                        "//*[@id='srpContainer']/div[2]/div[2]/div/div[2]/div/div[5]/div[1]/div/div/section["
                        + str(i + 1) + "]/div[2]/div/div[1]/div[1]/div/a/span").text):
                    listed = i+1
                    break
                else:
                    continue
            except NoSuchElementException:
                pass
        if listed == 0:
            while 1:
                divs = driver.find_element_by_tag_name('div').text
                if 'Mango Valley Resort Ganpatipule' in divs:
                    listed = str("%01d" % (i / 250))
                    driver.execute_script("window.scrollTo(" + str(i) + "," + str(i + 750) + ");")
                    time.sleep(1)
                    break
                else:
                    driver.execute_script("window.scrollTo(" + str(i) + "," + str(i + 250) + ");")
                    time.sleep(0.5)
                    i = i + 250
                    continue
        return listed
    
    def hotel_find(self, driver):
        element = driver.find_element_by_link_text("Mango Valley Resort Ganpatipule")
        driver.execute_script("arguments[0].click();", element)

    def data_scraping(self, driver):
        try:
            std_ep = driver.find_element_by_xpath("//*[@id='roomrtc_45000574650']/div/section/section[2]/aside[1]/"
                                                  "div[1]/div[3]/div[1]/p[2]/span").text
        except NoSuchElementException:
            std_ep = "--"
            pass
        try:
            std_cp = driver.find_element_by_xpath("//*[@id='roomrtc_45000574650']/div/section/section[2]/aside[2]/"
                                                  "div[1]/div[3]/div[1]/p[2]/span").text
        except NoSuchElementException:
            std_cp = "--"
            pass
        try:
            sup_ep = driver.find_element_by_xpath("//*[@id='roomrtc_45000574663']/div/section/section[2]/aside[1]"
                                                  "/div[1]/div[3]/div[1]/p[2]/span").text
        except NoSuchElementException:
            sup_ep = "--"
            pass
        try:
            sup_cp = driver.find_element_by_xpath("//*[@id='roomrtc_45000574663']/div/section/section[2]/aside[2]"
                                                  "/div[1]/div[3]/div[1]/p[2]/span").text
        except NoSuchElementException:
            sup_cp = "--"
            pass
        return std_ep, std_cp, sup_ep, sup_cp
