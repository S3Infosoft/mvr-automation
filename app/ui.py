from regular import main_run
from regular import MasterMMT
from local import*

def main():
    agent = Booking()
    # agent = Goibibo()
    agent = MasterMMT()
    search_text = "Ratnagiri"
    hotel_name = "Mango Valley Resort Ganpatipule"
    hotel_id = "4216443"
    checkin = "11/07/2019"
    checkout = "12/07/2019"
    room_typeids = ["room_type_id_421644301", "room_type_id_421644302",
                    "room_type_id_421644305", "room_type_id_421644303"]
    room_priceids = ["rate_price_id_421644301_141698786_0_0_0", "rate_price_id_421644301_174652031_0_2_0",
                     "rate_price_id_421644302_141698786_0_0_0", "rate_price_id_421644302_174652031_0_2_0",
                     "rate_price_id_421644305_174652031_4_2_0", "rate_price_id_421644303_174652031_0_2_0"]
    room_ids = ["roomrtc_45000574650", "roomrtc_45000574663", "roomrtc_45000653101", "roomrtc_45000574667"]
    # for booking
    print(main_run(agent, hotel_id, search_text, checkin, checkout,
                   room_typeids=room_typeids, room_priceids=room_priceids))
    # for goibibo
    # print(main_run(agent, hotel_name, search_text, checkin, checkout, room_ids=room_ids))
    # for mmt
    # print(MasterMMT.run(search_text, checkin, checkout))
