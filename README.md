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
  {"search_text":"Ratnagiri", "checkin_date": "26/10/2019", "checkout_date": "27/10/2019" }
  ```

- /automation/v1/goibibo
  ```
  {"search_text":"Ganpatipule", "checkin_date": "27/10/2019", "checkout_date": "28/10/2019" }
  ```

- /automation/v1/mmt
  ```
  {"search_text":"Ganpatipule", "checkin_date": "28/10/2019", "checkout_date": "29/10/2019" }
  ```
##### Expected Sample success and error response
- booking.com
  ```
  Invoked Booking.com API v1: {"Status": "OK", "Std_CP": "\u20b9 3,000", "Std_EP": "\u20b9 2,700", "Sup_CP": "\u20b9 4,000", "Sup_EP": "\u20b9 3,600", "check_in": "03/07/2019", "check_out": "04/07/2019", "listed_position": "1", "ota": "Booking", "run_time": "2019-07-02 08:15:22"}
  
  
  {"Status":"TIMEOUT ERROR"}
  ```
