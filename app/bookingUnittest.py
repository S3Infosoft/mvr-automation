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
        checkin = "30/03/2020"
        checkout = "31/03/2020"
        hotel_id = "4216443"
        current_time = datetime.datetime.now()
        end_date = current_time.strftime("%Y-%m-%d")
        room_typeids = ["room_type_id_421644306", "room_type_id_421644302",
                        "room_type_id_421644305", "room_type_id_421644303"]
        room_priceids = ["421644306_174652031_0_42_0",
                         "421644302_141698786_0_42_0", "421644302_174652031_0_42_0",
                         "421644305_174652031_0_42_0", "421644303_174652031_0_42_0"]
        self.result = main_run(self.agent, hotel_id, search_text, checkin, checkout, room_typeids=room_typeids,
                          room_priceids=room_priceids)


    # Testing Single Input Field.
    def test_TC1(self):
        assert "3" in self.result['listed_position']
        assert "['₹ 17,500']" in self.result['rates']['Superior Suite with Sea View']


    def test_TC2(self):
        assert "['₹ 17,507']" in self.result['rates']['Superior Suite with Sea View']

    # Closing the browser.
    def tearDown(self):
        pass

