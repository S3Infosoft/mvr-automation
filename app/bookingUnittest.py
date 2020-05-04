import unittest
from local import *
from regular import main_run
from regular import MasterMMT
from bookingdotcom import BookingDotComImpl
from goibibo import GoibiboImpl
from mmt import MMTImpl
import datetime

class BookingTest(unittest.TestCase):

    def setUp(self):
        self.agent = Booking()

        search_text = "Ratnagiri"
        hotel_name = "Mango Valley Resort Ganpatipule"
        checkin = "30/05/2020"
        checkout = "31/05/2020"
        hotel_id = "4216443"
        current_time = datetime.datetime.now()
        end_date = current_time.strftime("%Y-%m-%d")
        room_typeids = ["room_type_id_421644306", "room_type_id_421644302",
                        "room_type_id_421644305", "room_type_id_421644303"]
        room_priceids = ["421644306_174652031_0_42_0",
                         "421644302_141698786_0_42_0", "421644302_174652031_0_42_0",
                         "421644305_174652031_0_42_0", "421644303_174652031_0_42_0"]
        self.result = main_run(self.agent, hotel_id, search_text, checkin, checkout,hotel_name, room_typeids=room_typeids,
                          room_priceids=room_priceids)
        data1 = eval(self.result['rates']['Superior Suite with Sea View'])
        data1[0]=data1[0].replace('₹ ','')
        data1[0]=data1[0].replace(',', '')
        print(data1[0])

        self.data1 = float(data1[0])
        data2 = eval(self.result['rates']['Deluxe Bungalow with Sea View'])
        data2[0] = data2[0].replace('₹ ', '')
        data2[0] = data2[0].replace(',', '')
        self.data2 = float(data2[0])
        data3=self.result['rates']
        self.data3=len(data3)
        print(self.result)


    def test_TC1(self):
        assert self.data1>15000
        assert self.data2>5000
        assert self.data3==4


    def test_TC2(self):
        assert self.data1<15000

    # Closing the browser.
    # def tearDown(self):
    #     pass

