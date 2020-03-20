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
        hotel_name = "O'NEST Ganeshkrupa Deluxe"
        checkin = "30/04/2020"
        checkout = "31/04/2020"
        room_ids = ["roomrtc_45000750981", "roomrtc_45000574663", "roomrtc_45000717373",
                    "roomrtc_45000574667"]
        current_time = datetime.datetime.now()
        end_date = current_time.strftime("%Y-%m-%d")
        self.result = main_run(self.agent, hotel_name, search_text, checkin, checkout, room_ids=room_ids)
        data1 = eval(self.result['rates']['Rustic Villa with Breakfast'])
        self.data1 = data1[0]
        data2 = eval(self.result['rates']['Superior Double Room with Breakfast'])
        self.data2 = data2[0]

    # Testing Single Input Field.
    def test_TC1(self):
        print(self.result)
        assert self.data1>5000
        assert self.data2>4000



    def test_TC2(self):
        assert self.data1<3000




if __name__ == "__main__":
    unittest.main()