from ota import OTA
from Common import *
from local import Booking
from selenium.common.exceptions import TimeoutException


class BookingDotComImpl(OTA):
    def __init__(self, search_text, hotel_id, checkin, checkout, room_typeids, room_priceids):
        super(BookingDotComImpl, self).__init__("booking.com", checkin, checkout)
        self.search_text = search_text
        self.hotel_id = hotel_id
        self.room_typeids = room_typeids
        self.room_priceids = room_priceids

    def run(self):
        agent = Booking()
        agent_name = agent.__class__.__name__
        current_time = datetime.datetime.now()
        time1 = current_time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            return main_run(agent, self.hotel_id, self.search_text, self.checkin, self.checkout,
                            room_typeids=self.room_typeids, room_priceids=self.room_priceids)
        except TimeoutException:
            current_time = datetime.datetime.now()
            time2 = current_time.strftime("%Y-%m-%d %H:%M:%S")
            return {"ota": str(agent_name), "run_start_time": str(time1), "check_in": self.checkin,
                    "check_out": self.checkout, "run_end_time": str(time2), "Status": "TIMEOUT ERROR"}
        except Exception as e:
            current_time = datetime.datetime.now()
            time2 = current_time.strftime("%Y-%m-%d %H:%M:%S")
            return {"ota": str(agent_name), "run_start_time": str(time1), "check_in": self.checkin,
                    "check_out": self.checkout, "run_end_time": str(time2), "Status": str(e)}

        # TODO: Invoke specific run method with booking.com parameters
