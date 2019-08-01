from ota import OTA
from Common import *
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
        agent_name = agent.__class__.__name__
        current_time = datetime.datetime.now()
        time1 = current_time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            return main_run(agent, self.hotel_name, self.search_text,  self.checkin, self.checkout,
                            room_ids=self.room_ids)
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
