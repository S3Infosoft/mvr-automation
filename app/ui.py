from regular import main_run
from regular import MasterMMT
from local import*


def main():
    # agent = Booking()
    # agent = Goibibo()
    agent = MasterMMT()
    # search_text = "Ratnagiri" # for booking
    search_text = "Ganpatipule" #for goibibo & mmt
    hotel_name = "Mango Valley Resort Ganpatipule"
    checkin = "30/03/2020"
    checkout = "31/03/2020"
    # for booking
    # hotel_id = "4216443"
    #
    # room_typeids = ["room_type_id_421644306", "room_type_id_421644302",
    #                 "room_type_id_421644305", "room_type_id_421644303"]
    # room_priceids = ["421644306_174652031_0_42_0",
    #                  "421644302_141698786_0_42_0", "421644302_174652031_0_42_0",
    #                  "421644305_174652031_0_42_0", "421644303_174652031_0_42_0"]
    # result=main_run(agent, hotel_id, search_text, checkin, checkout,room_typeids=room_typeids, room_priceids=room_priceids)
    # if result['listed_position']=='3' and result['rates']['Superior Suite with Sea View']=="['₹ 17,500']" and result['rates']['Superior Double Room']=="['₹ 4,050', '₹ 4,500']" and result['rates']["Deluxe Bungalow with Sea View"]=="['₹ 7,600']" and result['rates']['Three-Bedroom Bungalow']=="['₹ 7,700']":
    #     print("Correct result generated and result is :")
    #     print(result)
    # else:
    #     print("Incorrect result generated and is: ")
    #     print(result)

    # for goibibo
    # room_ids = ["roomrtc_45000750981", "roomrtc_45000574663", "roomrtc_45000717373",
    #             "roomrtc_45000574667"]
    # result=main_run(agent, hotel_name, search_text, checkin, checkout, room_ids=room_ids)
    # if result['listed_position']=="15" and result['rates']['Rustic Villa with Breakfast'] == "['5035']" and result['rates']['Superior Double Room with Breakfast'] == "['4297']" and result['rates']['Sea View Villa2 with Breakfast']== "['5730']" and result['rates']['Villa Oceanica Garden View with Breakfast']=="['7274']":
    #     print("Correct result generated and result is :")
    #     print(result)
    # else:
    #     print("Incorrect result generated and is: ")
    #     print(result)

    # for mmt
    hotel_id = "201811281301162654"
    room_id = ["990001097019", "990001200931", "990001097020", "990001200939", "990001097021", "990001200965",
               "990001302537"]
    hotel_id = "201403202029134840"
    hotel_name = "Nakshatra Beach Resort by O'NEST"
    room_id = ["990000116124", "990000088134", "990000633744", "990000633727", "990001303500", "990000088158",
               "990000633761", "990001303499", "990000088270", "990000633777", "990001303498", "990000088272",
               "990000633793"]
    hotel_name = "Blue Ocean Resort & Spa"
    hotel_id = "200908241107085994"
    room_id = ["990000758441", "990000758470", "990000009534", "990000758436", "990000308366", "990000009536", "990000758437"]
    result=agent.run(search_text, hotel_id, hotel_name, checkin, checkout, room_id)
    if result['listed_position']=='4' and result['rates']['Standard Garden Room'] == "['INR 4,768', 'INR 5,172']" and result['rates']['Tropical garden Villa']=="['INR 6,601', 'INR 8,215']" and result['rates']['Executive Wing Room']=="['INR 8,435', 'INR 10,562']" and result['rates']['Beachfront Villa']=="['INR 11,410']":
        print("Correct result generated and result is :")
        print(result)
    else:
        print("Incorrect result generated and is: ")
        print(result)


if __name__ == "__main__":
    main()
