import unittest
from local import *
from regular import main_run
from regular import MasterMMT
from bookingdotcom import BookingDotComImpl
from goibibo import GoibiboImpl
from mmt import MMTImpl
import datetime

class MmtTest(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.agent = MasterMMT()
        search_text = "Ganpatipule"
        hotel_name = "Mango Valley Resort Ganpatipule"
        current_time = datetime.datetime.now()
        end_date = current_time.strftime("%Y-%m-%d")
        checkin = "30/03/20"
        checkout = "31/03/20"
        # hotel_id = "201811281301162654"
        # room_id = ["990001097019", "990001200931", "990001097020", "990001200939", "990001097021", "990001200965",
        #            "990001302537"]
        # hotel_id = "201403202029134840"
        # hotel_name = "Nakshatra Beach Resort by O'NEST"
        # room_id = ["990000116124", "990000088134", "990000633744", "990000633727", "990001303500", "990000088158",
        #            "990000633761", "990001303499", "990000088270", "990000633777", "990001303498", "990000088272",
        #            "990000633793"]
        hotel_name = "Blue Ocean Resort & Spa"
        hotel_id = "200908241107085994"
        room_id = ["990000758441", "990000758470", "990000009534", "990000758436", "990000308366", "990000009536",
                   "990000758437"]
        self.result = self.agent.run(search_text, hotel_id, hotel_name, checkin, checkout, room_id)


    # Testing Single Input Field.
    def test_TC1(self):
        print(self.result)
        assert "4" in self.result['listed_position']
        assert "['INR 5,031', 'INR 5,457']" in self.result['rates']['Standard Garden Room']


    def test_TC2(self):
        assert "['5038']" in self.result['rates']['Rustic Villa with Breakfast']




if __name__ == "__main__":
    unittest.main()