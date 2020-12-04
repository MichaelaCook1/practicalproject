#!/bin/bash
sudo apt update -y
sudo apt install python3-pip python3-venv -y

python3 -m venv venv
. venv/bin/activate
pip3 install flask flask-testing pytest pytest-cov requests Werkzeug==0.16.1 flask_sqlalchemy
pytest ./service1/testing/test_unit.py
pytest ./service2/testing/test_unit.py
pytest ./service3/testing/test_unit.py
pytest ./service4/testing/test_unit.py

deactivate
