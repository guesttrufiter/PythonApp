# Python Application Delivery Workflow

## Build & Test Guide
**Local Health Check:**
   ```bash
   python3 app.py // Starting the application server
   curl [http://127.0.0.1:5001/health](http://127.0.0.1:5001/health)  //Check health endpoint

**Run Unit Tests:**
    pytest // We use this for running automated unit tests

**Docker Containerization:**
    docker build -t python-cicd-app:v1 . // Building image
    docker run -d -p 5001:5001 --name python-app-instance python-cicd-app:v1 // Creating a container instance out of an image
    curl [http://127.0.0.1:5001/health](http://127.0.0.1:5001/health) // To test the the running container locally

**CI/CD Pipeline:**
    Automated testing runs on every push and pull request via GitHub Actions. // Github Actions to test ci.yml