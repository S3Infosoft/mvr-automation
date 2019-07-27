from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time


class Booking(object):
    target = "https://www.booking.com/"
    search_id = "ss"
    calender = "span.sb-date-field__icon.sb-date-field__icon-btn.bk-svg-wrapper.calendar-restructure-sb"
    week_finder = "//*[@id='frm']/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr["

    @staticmethod
    def day_in(weekin, datein):
        return "//*[@id='frm']/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr["\
               + weekin + "]/td[@data-date='" + datein + "']"

    @staticmethod
    def day_out(weekout, dateout):
        return "//*[@id='frm']/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr["\
               + weekout + "]/td[@data-date='" + dateout + "']"

    @staticmethod
    def proceed(driver):
        # driver.find_element_by_xpath(Booking.search_id).send_keys(Keys.ENTER)
        pass

    @staticmethod
    def listing(driver, hotel_id):
        listed = "-"
        for i in range(40):
            if ((driver.find_element_by_xpath("//*[@id='hotellist_inner']/div[@data-hotelid='"+hotel_id+"']")) == (
                 driver.find_element_by_xpath("//*[@id='hotellist_inner']/div[" + str(i + 1) + "]"))):
                listed = str("%01d" % ((i + 1) / 2))
                break
        return listed

    @staticmethod
    def hotel_find(driver, hotel_id):
        path = "//*[@id='hotellist_inner']/div[@data-hotelid='"+hotel_id+"']"
        driver.find_element_by_xpath(path).click()

    @staticmethod
    def data_scraping(driver, **kwargs):
        room_priceids = None
        room_typeids = None
        for key, value in kwargs.items():
            if key == "room_typeids":
                room_typeids = value
            if key == "room_priceids":
                room_priceids = value
        room_type = []
        room_price = []
        for i in range(len(room_typeids)):
            room_price.append([])
            room_type.append(driver.find_element_by_id(room_typeids[i]).get_attribute("data-room-name"))
            for j in range(len(room_priceids)):
                if room_typeids[i].split("_")[3] == room_priceids[j].split("_")[3]:
                    room_price[i].append(driver.find_element_by_id(room_priceids[j]).text)
        returnlist = []
        for i in range(len(room_type)):
            returnlist.append(room_type[i])
            returnlist.append(room_price[i])
        return returnlist


class Goibibo(object):
    target = "https://www.goibibo.com/hotels/"
    search_id = "gosuggest_inputL"
    calender = "input.form-control.inputTxtLarge.widgetCalenderTxt"
    week_finder = "//*[@id='Home']/div[3]/div[1]/div/div[1]/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[3]/div["

    @staticmethod
    def day_in(weekin, datein):
        _, _, cin = datein.split("-")
        cin = str("%01d" % int(cin))
        return "//*[@id='Home']/div[3]/div[1]/div/div[1]/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[3]/div["\
               + weekin + "]/div[text()='" + cin + "']"

    @staticmethod
    def day_out(weekout, dateout):
        _, _, cout = dateout.split("-")
        cout = str("%01d" % int(cout))
        return "//*[@id='Home']/div[3]/div[1]/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[2]/div[3]/div["\
               + weekout + "]/div[text()='" + cout + "']"

    @staticmethod
    def proceed(driver):
        waiting = WebDriverWait(driver, 10)
        element = waiting.until(ec.visibility_of_element_located(
            (By.XPATH, "//li[@id = 'react-autosuggest-1-suggestion--0']/div[1]/div[1]/div[1]/span")))
        element.click()
        driver.find_element_by_xpath("//*[@id='Home']/div[3]/div[1]/div/div[1]/div[3]/div/div[3]/div/button").click()

    @staticmethod
    def listing(driver, hotel_name):
        i = 0
        listed = 0
        for i in range(3):
            try:

                if (hotel_name == driver.find_element_by_xpath(
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
                if hotel_name in divs:
                    listed = "%01d" % (i / 250)
                    driver.execute_script("window.scrollTo(" + str(i) + "," + str(i + 750) + ");")
                    time.sleep(1)
                    break
                else:
                    driver.execute_script("window.scrollTo(" + str(i) + "," + str(i + 250) + ");")
                    time.sleep(0.5)
                    i = i + 250
                    if i > 7500:
                        break
                    else:
                        continue
        # print(listed)
        return str(listed)

    @staticmethod
    def hotel_find(driver, hotel_name):
        element = driver.find_element_by_link_text(hotel_name)
        # time.sleep(1)
        driver.execute_script("arguments[0].click();", element)

    @staticmethod
    def data_scraping(driver, **kwargs):
        room_ids = None
        for key, value in kwargs.items():
            if key == "room_ids":
                room_ids = value
        room_type = []
        room_price = []
        returnlist = []
        for i in range(len(room_ids)):
            room_price.append([])
            room_type.append(driver.find_element_by_xpath("//*[@id='"+room_ids[i] +
                                                          "']/div/section/section[2]/aside[1]/div[1]/div[2]/p[1]").text)
            try:
                room_price[i].append(driver.find_element_by_xpath(
                    "//*[@id='"+room_ids[i]+"']/div/section/section[2]/aside[1]/div[1]/div[3]/div[1]/p[2]/span").text)
            except NoSuchElementException:
                pass
            try:
                room_price[i].append(driver.find_element_by_xpath("//*[@id='" + room_ids[i] +
                                                                  "']/div/section/section[2]/aside[2]/"
                                                                  "div[1]/div[3]/div[1]/p[2]/span").text)
            except NoSuchElementException:
                pass
        for i in range(len(room_type)):
            returnlist.append(room_type[i])
            returnlist.append(room_price[i])
        return returnlist


class Mmt(object):
    @staticmethod
    def listing(driver, hotel_id, search_text, din, dout):
        cin, month, year = din.split("/")
        cout, month, year = dout.split("/")
        driver.get("https://www.makemytrip.com/hotels/hotel-listing/?checkin=" + month + cin + year +
                   "&checkout=" + month + cout + year + "&city=XGP&country=IN&searchText=" + search_text +
                   "%2C%20India&roomStayQualifier=2e0e")
        a = driver.find_element_by_xpath("//*[@id='htl_id_seo_"+hotel_id+"']")
        # a = driver.find_element_by_link_text("Mango Valley Resort Ganpatipule")
        i = 0
        time.sleep(2)
        while 1:
            try:
                b = driver.find_element_by_xpath(
                    "//*[@id='Listing_hotel_" + str(i) + "']/a/div/div[1]/div[2]/div[2]/div[1]/p/span")
            except NoSuchElementException:
                b = driver.find_element_by_xpath(
                    "//*[@id='Listing_hotel_" + str(i) + "']/a/div/div[1]/div[2]/div[1]/div[1]/p/span")
            if a == b:
                return str(i + 1)
            else:
                i = i + 1

    @staticmethod
    def hotel_find(driver, hotel_id, hotel_name, din, dout):
        cin, month, year = din.split("/")
        cout, month, year = dout.split("/")
        hotel_name.replace(" ", "%20")
        driver.get("https://www.makemytrip.com/hotels/hotel-details/?checkin=" + month + cin + year +
                   "&hotelId="+hotel_id+"&pType=details&screenType=details&checkout=" + month + cout + year +
                   "&roomStayQualifier=2e0e&city=XGP&country=IN&type=HTL&searchText="+hotel_name +
                   "&visitorId=0d107fed-19ac-481f-8e43-163a944ac760")

    @staticmethod
    def data_scraping(driver, room_id):
        room_type = []
        room_price = []
        m = 0
        for i in range(4):
            try:
                room_price.append([])
                room_type.append(driver.find_element_by_xpath("//*[@id='RoomType']/div/div[2]/div["
                                                              + str(i+2)+"]/div[1]/div/h2").text)
                for j in range(2):
                    room_price[i].append(driver.find_element_by_xpath("//*[@id='"+room_id[m] +
                                                                      "']/div[2]/div[1]/div/span[1]").text)
                    m = m+1
                    if m >= len(room_id):
                        break
            except NoSuchElementException:
                pass
        returnlist = []
        for i in range(len(room_type)):
            returnlist.append(room_type[i])
            returnlist.append(room_price[i])
        return returnlist
