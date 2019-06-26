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

##### JSON Input Format for calling run method:
 ```
 {"ota_name":"booking.com", "month": "June","year":"2019", "cin":"22","cout":"24"}
 ```
