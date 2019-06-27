
from ota import OTA

class GoibiboImpl(OTA):
    def __init__(self, place, checkin, checkout):
        super(GoibiboImpl, self).__init__("goibibo.com", checkin, checkout)
        self.place = place
        self.result = {}
        self.result['checkin'] = checkin
        self.result['checkout'] = checkout
        self.result['place'] = place
        self.result['status'] = 'OK'

    def run(self):
        # TODO: Invoke specific run method with goibibo parameters
        return self.result
