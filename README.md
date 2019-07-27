# mvr-automation
MVR Channel Automation via Selenium

#### Docker Steps
- Go to the project directory
  ```
  cd mvr-automation
  ```
- Build image and selenium hub
  ```
  docker-compose build
  ```
- Execute
  ```
  docker-compose up
  ```

##### API Invocation

- /automation/v1/booking
  ```
  {"search_text":"Ratnagiri", "hotel_id": "4216443","checkin_date": "26/10/2019", "checkout_date": "27/10/2019","room_typeids":["room_type_id_421644301", "room_type_id_421644302", "room_type_id_421644305", "room_type_id_421644303"],"room_priceids":["rate_price_id_421644301_141698786_0_0_0", "rate_price_id_421644301_174652031_0_2_0","rate_price_id_421644302_141698786_0_0_0", "rate_price_id_421644302_174652031_0_2_0","rate_price_id_421644305_174652031_4_2_0", "rate_price_id_421644303_174652031_0_2_0"]}
  ```

- /automation/v1/goibibo
    ```
  {"search_text":"Ganpatipule", "hotel_name": "Mango Valley Resort Ganpatipule","checkin_date": "26/07/2019", "checkout_date": "27/07/2019","room_ids":["roomrtc_45000574650", "roomrtc_45000574663", "roomrtc_45000653101", "roomrtc_45000574667"]}
   ```

- /automation/v1/mmt
  ```
  {"search_text":"Ganpatipule","hotel_id":"201811281301162654","hotel_name":"Mango Valley Resort Ganpatipule", "checkin_date": "28/10/2019", "checkout_date": "29/10/2019","room_id":["990001097019", "990001200931", "990001097020", "990001200939", "990001097021", "990001200965","990001302537"] }
  ```
##### Expected Sample success and error response
- booking.com
  ```
  Invoked Booking.com API v1: {"Status": "OK", "Std_CP": "\u20b9 3,000", "Std_EP": "\u20b9 2,700", "Sup_CP": "\u20b9 4,000", "Sup_EP": "\u20b9 3,600", "check_in": "03/07/2019", "check_out": "04/07/2019", "listed_position": "1", "ota": "Booking", "run_time": "2019-07-02 08:15:22"}
  
- MMT
  ```
  {"Status": "OK", "check_in": "28/10/2019", "check_out": "29/10/2019", "listed_position": "6", "ota": "Mmt", "rates": {"Standard Double Room": "['INR 2,610', 'INR 2,871']", "Superior Double Room": "['INR 3,480', 'INR 3,759']", "Villa Oceanica Garden View": "['INR 6,525', 'INR 7,178']", "Villa Oceanica Sea View": "['INR 6,525']"}, "run_time": "2019-07-27 04:06:21"}
  
  
  {"Status":"TIMEOUT ERROR"}
  ```
