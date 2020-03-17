import unittest
from local import *
from regular import main_run
from regular import MasterMMT
from bookingdotcom import BookingDotComImpl
from goibibo import GoibiboImpl
from mmt import MMTImpl
import datetime



class GoibiboTest(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.agent = Goibibo()
        search_text = "Ganpatipule"
        hotel_name = "Mango Valley Resort Ganpatipule"
        checkin = "30/03/2020"
        checkout = "31/03/2020"
        room_ids = ["roomrtc_45000750981", "roomrtc_45000574663", "roomrtc_45000717373",
                    "roomrtc_45000574667"]
        current_time = datetime.datetime.now()
        end_date = current_time.strftime("%Y-%m-%d")
        self.result = main_run(self.agent, hotel_name, search_text, checkin, checkout, room_ids=room_ids)


    # Testing Single Input Field.
    def test_TC1(self):
        print(self.result)
        assert "15" in self.result['listed_position']
        assert "['5172']" in self.result['rates']['Rustic Villa with Breakfast']


    def test_TC2(self):
        assert "['5038']" in self.result['rates']['Rustic Villa with Breakfast']




if __name__ == "__main__":
    unittest.main()