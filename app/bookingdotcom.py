from ota import OTA
from Common import main_run
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
        try:
            return main_run(agent, self.hotel_id, self.search_text,self.checkin, self.checkout,
                            room_typeids=self.room_typeids, room_priceids=self.room_priceids)
        except TimeoutException:
            return {"Status": "TIMEOUT ERROR"}
        except Exception as e:
            return {"Status": str(e)}
        # TODO: Invoke specific run method with booking.com parameters
