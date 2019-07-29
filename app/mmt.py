from Common import *
from local import Mmt
from selenium.common.exceptions import TimeoutException
from ota import OTA


class MMTImpl(OTA):
    def __init__(self, search_text, hotel_id, hotel_name, checkin, checkout, room_id):
        super(MMTImpl, self).__init__("MMT", checkin, checkout)
        self.search_text = search_text
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name
        self.room_id = room_id

    def run(self):
        # TODO: Invoke specific run method with MMT parameters
        agent = Mmt()
        try:
            agent_name = agent.__class__.__name__
            driver = start_driver()
            listed = agent.listing(driver, self.hotel_id, self.search_text, self.checkin, self.checkout)
            driver.quit()
            driver = start_driver()
            agent.hotel_find(driver, self.hotel_id, self.hotel_name, self.checkin, self.checkout)
            data = agent.data_scraping(driver, self.room_id)
            driver.quit()
            returndata = sql_entry(listed, agent_name, self.checkin, self.checkout, data)
            return returndata
        except TimeoutException:
            return {"Status": "TIMEOUT ERROR"}
        except Exception as e:
            return {"Status": e}
