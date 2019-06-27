
from ota import OTA

class MMTImpl(OTA):
    def __init__(self, place, checkin, checkout):
        super(MMTImpl, self).__init__("MMT", checkin, checkout)
        self.place = place
        self.result = {}
        self.result['checkin'] = checkin
        self.result['checkout'] = checkout
        self.result['place'] = place
        self.result['status'] = 'OK'

    def run(self):
        # TODO: Invoke specific run method with MMT parameters
        return self.result
