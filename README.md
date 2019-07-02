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
