from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


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
        # driver.find_element_by_xpath("//*[@id='frm']/div[1]/div[4]/div[2]/button").send_keys(Keys.ENTER) #its my code
        pass

    @staticmethod
    def listing(driver, hotel_id):
        listed = "-"
        for i in range(40):
                wait = WebDriverWait(driver, 10)
                wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='hotellist_inner']/div[@data-hotelid='"+hotel_id+"']")))
                print(driver.find_element_by_xpath("//*[@id='hotellist_inner']/div[@data-hotelid='"+hotel_id+"']"))
                print(driver.find_element_by_xpath("//*[@id='hotellist_inner']/div[" + str(i + 1) + "]"))
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
                if room_typeids[i].split("_")[3] == room_priceids[j].split("_")[0]:
                    try:
                        a=driver.find_element_by_id("hprt_nos_select_" + room_priceids[j]).text

                        ele=a
                        s1=ele.find('(')
                        s2=ele.find(')')
                        pr=ele[s1+1:s2]


                        # room_price[i].append(driver.find_element_by_id("hprt_nos_select_"+room_priceids[j]).text)
                        room_price[i].append(pr)
                        # print(driver.find_element_by_xpath("//*[@id=hprt_nos_select_"+room_priceids[j]+"]/option[2]").text)
                        #  driver.find_element_by_xpath("//*[@id=hprt_nos_select_"+room_priceids[j]+"]/option[2]").click()
                        #  print("ab")

                         # print(driver.find_element_by_xpath("//*[@data-block-id="+room_priceids[j]+"]/td[3]/div/div[2]/div[1]"))
                         # room_price[i].append(driver.find_element_by_xpath("//*[@data-block-id="+room_priceids[j]+"]/td[3]/div/div[2]/div[1]").text)
                    # // *[ @ id = "hprt-table"] / tbody / tr[6] / td[3] / div / div[2] / div[1]
                    except NoSuchElementException:
                        print("error")
                        pass
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
        for i in range(10):

            if driver.find_element_by_xpath(f"//li[@id= 'react-autosuggest-1-suggestion--{i}']/div[1]/div[1]/div[1]/span").text=='Ganpatipule':
                driver.find_element_by_xpath(f"//li[@id= 'react-autosuggest-1-suggestion--{i}']/div[1]/div[1]/div[1]/span").click()
                print('b')
                break
        driver.find_element_by_xpath("//*[@id='Home']/div[3]/div[1]/div/div[1]/div[3]/div/div[3]/div/button").click()

    @staticmethod
    def listing(driver, hotel_name):
        try:
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

        except IndexError as e:
                print(e,listed,e.args)
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
            # // *[ @ id = "roomrtc_45000750981"] / div / section / section[2] / aside[2] / div / div[1] / p[1]
            # room_type.append(driver.find_element_by_xpath("//*[@id='"+room_ids[i] + "']/div/section/section[2]/aside[1]/div[1]/div[2]/p[1]").text)
            room_type.append(driver.find_element_by_xpath("//*[@id='"+room_ids[i] + "']/div/section/section[2]/aside/div/div/p[1]").text)
            # // *[ @ id = 'roomrtc_45000234216'] / div / section / section[2] / aside / div / div / p[1]
            try:
                # // *[ @ id = "roomrtc_45000750981"] / div / section / section[2] / aside[2] / div / div[2] / div[1] / p[2] / span
                # room_price[i].append(driver.find_element_by_xpath("//*[@id='"+room_ids[i]+"']/div/section/section[2]/aside[1]/div[1]/div[3]/div[1]/p[2]/span").text)
                room_price[i].append(driver.find_element_by_xpath("//*[@id='"+room_ids[i] +"']/div/section/section[2]/aside/div/div/div[1]/p[2]/span").text)
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

class NewGoibibo(object):
    target = "https://www.goibibo.com/hotels/"
    search_id = "downshift-1-input"
    calender = "input.form-control.inputTxtLarge.widgetCalenderTxt"
    week_finder = "//*[@id='Home']/div[3]/div[1]/div/div[1]/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[3]/div["

    @staticmethod
    def day_in(driver, datein):
        _, _, cin = datein.split("-")
        cin = str("%01d" % int(cin))
        for i in range(1,8):
            if driver.find_element_by_xpath(f'//*[@id="root"]/section/div/div[3]/section[1]/div[1]/div[2]/div[3]/div/div[4]/div/div/div[2]/div[1]/div/ul[2]/li[{i}]/span').text =='':
                continue
            else:
                break
        cin=int(cin)+i-1

        return f'//*[@id="root"]/section/div/div[3]/section[1]/div[1]/div[2]/div[3]/div/div[4]/div/div/div[2]/div[1]/div/ul[2]/li[{cin}]/span'

    @staticmethod
    def day_out(driver, dateout):
        _, _, cout = dateout.split("-")
        cout = str("%01d" % int(cout))
        for i in range(1, 8):
            if driver.find_element_by_xpath(
                    f'//*[@id="root"]/section/div/div[3]/section[1]/div[1]/div[2]/div[3]/div/div[4]/div/div/div[2]/div[1]/div/ul[2]/li[{i}]/span').text == '':
                continue
            else:
                break
        cout = int(cout) + i - 1

        return f'//*[@id="root"]/section/div/div[3]/section[1]/div[1]/div[2]/div[3]/div/div[4]/div/div/div[2]/div[1]/div/ul[2]/li[{cout}]/span'





    @staticmethod
    def proceed(driver):
        waiting = WebDriverWait(driver, 10)
        element = waiting.until(ec.visibility_of_element_located(
        (By.XPATH, '//*[@id="downshift-1-item-0"]/span')))
        for i in range(10):
            # waiting = WebDriverWait(driver, 10)
            # element = waiting.until(ec.visibility_of_element_located(
            # (By.XPATH, f'//*[@id="downshift-1-item-{i}"]/span')))
            print(i)
            if driver.find_element_by_xpath(f'//*[@id="downshift-1-item-{i}"]/span').text == 'Ganpatipule':
                driver.find_element_by_xpath(f'//*[@id="downshift-1-item-{i}"]/span').click()
                break
        driver.find_element_by_xpath('//*[@id="root"]/section/div/div[3]/section[1]/div[1]/div/button').click()

    @staticmethod
    def listing(driver, hotel_name):
        try:
            i = 0
            listed = 0
            for i in range(3):

                try:
                    waiting = WebDriverWait(driver, 10)
                    element = waiting.until(ec.visibility_of_element_located(
                        (By.XPATH, '//*[@id="root"]/span/div/section[2]/div/div/div[' + str(
                        i + 2) + ']/div/div[3]/div[1]/div[1]/div[2]/span')))

                    if (hotel_name == driver.find_element_by_xpath(
                            '//*[@id="root"]/span/div/section[2]/div/div/div['+str(i+2)+']/div/div[3]/div[1]/div[1]/div[2]/span').text):

                        listed = i+1
                        break
                    else:
                        continue
                except NoSuchElementException as e:
                    print("error e3 : ",e.args )
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
            print(listed)

            return str(listed)

        except IndexError:
                return str(listed)

    @staticmethod
    def hotel_find(driver, hotel_name,listed):
        l = driver.find_elements_by_class_name('HotelCardstyles__HotelNameTextSpan-sc-1s80tyk-14')
        print(l)
        for i in range(int(listed) + 1):
            if l[i].text == hotel_name:
                l[i].click()
                print('b')
                time.sleep(2)
                break



    @staticmethod
    def data_scraping(driver):
        room_ids = None
        # print('a')
        room_type = []
        room_price = []
        room_type_refrences = driver.find_elements_by_xpath('//*[@class="RoomFlavors__RoomFlavorsContainer-ikuviz-0 ihqqYP room-flavor-container"]')
        print(room_type_refrences,type(room_type_refrences))
        # room_price_refrences=driver.find_elements_by_class_name('')
        count=len(room_type_refrences)
        for i in range(count):
            r_type=driver.find_element_by_xpath(f'// *[ @ id = "rooms"] / div[{i+2}] / div / div[1]/ div/ p').text
            # print(r_type)
            r_price=driver.find_element_by_xpath(f'//*[ @ id = "rooms"]/div[{i+2}]//*[@class="RoomFlavor__ActualPriceTextStyled-guj4pt-13 cDymtq"]').text
            # print(r_price,r_type)
            room_type.append(r_type)
            room_price.append(r_price)



        returnlist = []

        for i in range(len(room_type_refrences)):
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
        driver.maximize_window();
        wait = WebDriverWait(driver, 10)
        wait.until(ec.visibility_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/div[3]/div[2]')))
        driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[2]').click()
        driver.find_element_by_xpath("//*[@id='hsw_search_button']").click()
        # wait = WebDriverWait(driver, 10)
        # wait.until(ec.visibility_of_element_located(
        #     (By.XPATH, '//*[@id="htl_id_seo_'+hotel_id+'"]')))
        # a = driver.find_element_by_xpath('//*[@id="htl_id_seo_' + hotel_id + '"]')
        n=0
        while n<40:
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            try:
                a = driver.find_element_by_xpath('//*[@id="htl_id_seo_'+hotel_id+'"]')
                break
            except:
                n+=1
                continue
        # print(f"a={a} and a text = {a.text}")

        i = 0
        time.sleep(2)
        while 1:
            try:
                b = driver.find_element_by_xpath(
                    "//*[@id='Listing_hotel_" + str(i) + "']/a/div/div[1]/div[2]/div[2]/div[1]/p/span")
            except NoSuchElementException:
                b = driver.find_element_by_xpath(
                    "//*[@id='Listing_hotel_" + str(i) + "']/a/div/div[1]/div[2]/div[1]/div[1]/p/span")
            print(f"b={b} and b text = {b.text}")
            try:
                if a == b:
                    return str(i + 1)
                else:
                    i = i + 1
            except Exception as e:
                if str(e) == "local variable 'a' referenced before assignment":
                     return 0

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
        print('a')
        m = 0
        time.sleep(5)
        for i in range(4):
            try:

                room_price.append([])
                room_type.append(driver.find_element_by_xpath("//*[@id='RoomType']/div/div[2]/div["
                                                              + str(i+2)+"]/div[1]/div/h2").text)
                k = 1
                try:
                    while k < len(room_id):
                        driver.find_element_by_xpath("//*[@id='RoomType']/div/div[2]/div["
                                             + str(i + 2) + "]/div[2]/div[" + str(k) + "]")
                        k = k+1
                except NoSuchElementException:
                    count = k - 1
                except Exception as e:
                    print(e,e.args)

                for j in range(count):
                    wait = WebDriverWait(driver, 10)
                    wait.until(ec.visibility_of_element_located(
                        (By.XPATH, "//*[@id='"+room_id[m] +
                                          "']/div[2]/div[1]/div/span[1]")))

                    room_price[i].append(driver.find_element_by_xpath("//*[@id='"+room_id[m] +
                                                                      "']/div[2]/div[1]/div/span[1]").text)
                    m = m+1
                    if m >= len(room_id):
                        break
            except NoSuchElementException as e:
                print(i,e.args)
                pass
            except Exception as e:
                print(e,e.args)
        returnlist = []
        for i in range(len(room_type)):
            returnlist.append(room_type[i])
            returnlist.append(room_price[i])
        print(returnlist)
        return returnlist
