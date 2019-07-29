from ota import OTA
from Common import main_run
from local import Goibibo
from selenium.common.exceptions import TimeoutException


class GoibiboImpl(OTA):
    def __init__(self, search_text, hotel_name, checkin, checkout, room_ids):
        super(GoibiboImpl, self).__init__("goibibo.com", checkin, checkout)
        self.search_text = search_text
        self.hotel_name = hotel_name
        self.room_ids = room_ids

    def run(self):
        # TODO: Invoke specific run method with goibibo parameters
        agent = Goibibo()
        try:
            return main_run(agent, self.hotel_name, self.search_text,  self.checkin, self.checkout,
                            room_ids=self.room_ids)
        except TimeoutException:
            return {"Status": "TIMEOUT ERROR"}
        except Exception as e:
            return {"Status": e}
