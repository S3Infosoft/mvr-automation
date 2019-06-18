# mvr-automation
Automation files - MVR

#### Docker Steps
- Go to the project directory
  ```
  cd mvr-automation/src
  ```
- Build the Docker image
  ```
  docker build -t mvr-automation:latest .
  ```
- Execute
  ```
  docker run --rm -p 5000:5000 -d --name s3infosoft mvr-automation:latest
  ```

