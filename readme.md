# Python Application Delivery Workflow

## Build & Test Guide
**Local Health Check:**
   ```bash
   python3 app.py
   curl [http://127.0.0.1:5001/health](http://127.0.0.1:5001/health)

**Run Unit Tests:**
    pytest

**Docker Containerization:**
    docker build -t python-cicd-app:v1 .
    docker run -d -p 5001:5001 --name python-app-instance python-cicd-app:v1
    curl [http://127.0.0.1:5001/health](http://127.0.0.1:5001/health)

**CI/CD Pipeline:**
    Automated testing runs on every push and pull request via GitHub Actions.