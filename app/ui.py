from regular import main_run
from regular import MasterMMT
from regular import main_run_for_new_goibibo
from local import*


def main():
    booking_run()
    # goibibo_run()
    # mmt_run()

def goibibo_run( checkin = "29/04/2020",checkout = "30/04/2020"):
    agent = Goibibo()
    search_text = "Ganpatipule"  # for goibibo & mmt
    hotel_name = "Mango Valley Resort Ganpatipule"
    hotel_name = "O'NEST Nakshatra Beach Resort"  # for goibibo
    # below are room ids for Mango valley resort
    room_ids = ["roomrtc_45000750981", "roomrtc_45000574663", "roomrtc_45000717373",
                "roomrtc_45000574667"]
    # below are room ids for O'O'NEST Nakshatra Beach Resort
    room_ids = ["roomrtc_45000234216", "roomrtc_45000065190", "roomrtc_45000065292"]

    try:
        result = main_run(agent, hotel_name, search_text, checkin, checkout,hotel_name,
                          room_ids=room_ids)  # it returns the driver if the interface is new one
        result['listed_position']  # this statement is not a dummy statement instead it checks weather the result is driver object or not if it is driver object then it will raise 'WebDriver' object is not subscriptable type error that we handle in try block
    except Exception as e:
        try:
            # print(e)
            e1 = str(e)
            # print(e, type(e))
            if e1 == "'WebDriver' object is not subscriptable":

                try:
                    driver = result
                    result = main_run_for_new_goibibo(driver, agent, hotel_name, search_text, checkin, checkout,hotel_name,
                                                      room_ids=room_ids)
                except Exception as e2:
                    print("e2 error is : ", e2.args)
            # elif e1==
        except Exception as e3:
            print("e1 error is: ", e3.args)
    print(result)
    return result

def booking_run(checkin = "26/05/2020",checkout = "15/06/2020"):
    agent = Booking()
    search_text = "Ratnagiri"
    hotel_name = "Mango Valley Resort Ganpatipule"
    hotel_id = "4216443"
    room_typeids = ["room_type_id_421644306", "room_type_id_421644302",
                    "room_type_id_421644305", "room_type_id_421644303"]
    room_priceids = ["421644306_174652031_0_42_0",
                     "421644302_141698786_0_42_0", "421644302_174652031_0_42_0",
                     "421644305_174652031_0_42_0", "421644303_174652031_0_42_0"]

    # hotel_name="The Blue View - sea view villa's"
    # hotel_id="2808749"
    # room_typeids=[
    # #    'room_type_id_280874901']
                  # 'room_type_id_280874905']
    # room_priceids=[
       ## '280874901_229832000_0_41_0']
        # '280874905_229832000_0_41_0']
    result=main_run(agent, hotel_id, search_text, checkin, checkout,hotel_name,room_typeids=room_typeids, room_priceids=room_priceids)
    print(result)
    return result

def mmt_run(checkin = "29/04/2020", checkout = "30/05/2020"):
    agent = MasterMMT()
    search_text = "Ganpatipule"
    hotel_name = "Mango Valley Resort Ganpatipule"
    hotel_id = "201811281301162654"
    room_id = ["990001097020", "990001200939", "990001097021", "990001200965",
               "990001302537","990001535696","990001535697","990001460104",'990001460107','990001433579','990001433580']
    # hotel_id = "201403202029134840"
    # hotel_name = "Nakshatra Beach Resort by O'NEST"
    # room_id = ["990000116124", "990000088134", "990000633744", "990000633727", "990001303500", "990000088158",
    #            "990000633761", "990001303499", "990000088270", "990000633777", "990001303498", "990000088272",
    #            "990000633793"]
    hotel_name = "Blue Ocean Resort & Spa"
    hotel_id = "200908241107085994"
    room_id = ["990000758441", "990000758470", "990000009534", "990000758436", "990000308366", "990000009536", "990000758437"]
    result=agent.run(search_text, hotel_id, hotel_name, checkin, checkout, room_id)
    print(result)
    return result

if __name__ == "__main__":
    main()
