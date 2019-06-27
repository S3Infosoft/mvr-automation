
from ota import OTA

class BookingDotComImpl(OTA):
    def __init__(self, property_id, checkin, checkout):
        super(BookingDotComImpl, self).__init__("booking.com", checkin, checkout)
        self.property_id = property_id
        self.result = {}
        self.result['checkin'] = checkin
        self.result['checkout'] = checkout
        self.result['property'] = property_id
        self.result['status'] = 'OK'

    def run(self):
        # TODO: Invoke specific run method with booking.com parameters
        return self.result
