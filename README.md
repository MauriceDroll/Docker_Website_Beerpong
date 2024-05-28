# How to Start

source start_docker.sh

# navigate to the folder: src/pkg_website_beerpong
start it with: python3 app.py

# Ongoing problem, website crashes if in one session a second table is clicked
-> Publisher of ROs is the problem (SelectTablePublisher) 
-> rclpy is not correctly shutdown (seems to be the problem).


# How to access the website

navigate in your browser to: http://127.0.0.1:8080/
