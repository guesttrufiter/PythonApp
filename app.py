"""
Application: Python CI/CD Flask Service
Description: A simple Flask application featuring a home endpoint and a health check endpoint.
Designed for containerization with Docker and automated testing via GitHub Actions.
"""

from flask import Flask, jsonify

# Initialize the Flask application instance
app = Flask(__name__)

@app.route("/")
def home():
    """
    Home endpoint that returns a welcome JSON message.
    Used to verify general application routing.
    """
    return jsonify({"message": "Welcome to the Python CI/CD App"})

@app.route("/health")
def health_check():
    """
    Health check endpoint that returns a healthy JSON status.
    Used by container probes and CI checks to confirm app stability.
    """
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    # Run the application on all interfaces (0.0.0.0) at port 5001 for local/container execution
    app.run(host="0.0.0.0", port=5001, debug=True)