# Flask App for Monitoring CPU and RAM Usage

This is a simple Flask app that reports the current CPU and RAM usage of the server. The app uses the `psutil` library to gather system resource information.

## Getting Started

To run the app, you'll need to install the required Python packages using the `requirements.txt` file. You can do this by running the following command in the terminal:

pip install -r requirements.txt

Once the packages are installed, you can start the app using the following command:

python app.py


This will start the app on `http://localhost:5000/`, where you can view the current CPU and RAM usage.

## Docker

You can also run the app in a Docker container. To build the Docker image, navigate to the directory containing the Dockerfile and run the following command:

docker build -t flask-cpu-ram-monitor .

This will build the Docker image with the tag `flask-cpu-ram-monitor`. You can then run the Docker image using the following command:

docker run -p 5000:5000 flask-cpu-ram-monitor

This will start a container running the Flask app and map port 5000 in the container to port 5000 on your host machine. You can then navigate to `http://localhost:5000` in your web browser to see the CPU and RAM usage information.

## Requirements

The required Python packages are listed in the `requirements.txt` file. You can install them using the command:

pip install -r requirements.txt
