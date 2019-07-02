from ota import OTA
from Common import main_run
from local import Booking
from selenium.common.exceptions import TimeoutException


class BookingDotComImpl(OTA):
    def __init__(self, search_text, checkin, checkout):
        super(BookingDotComImpl, self).__init__("booking.com", checkin, checkout)
        self.search_text = search_text

    def run(self):
        agent = Booking()
        try:
            return main_run(agent, self.search_text, self.checkin, self.checkout)
        except TimeoutException:
            return {"Status": "TIMEOUT ERROR"}
        # TODO: Invoke specific run method with booking.com parameters
