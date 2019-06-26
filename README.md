# mvr-automation
MVR Channel Automation via Selenium

#### Docker Steps
- Go to the project directory
  ```
  cd mvr-automation
  ```
- Build the Docker image
  ```
  docker build -t mvr-automation:latest .
  ```
- Execute
  ```
  docker run --rm -p 5000:5000 -d --name s3infosoft mvr-automation:latest
  ```
- Check logs
  ```
  docker logs [container id]
  ```
 # JSON Input Format for calling run method:
 ```
 {"ota_name":"booking.com", "month": "June","year":"2019", "cin":"22","cout":"24"}
 ```
