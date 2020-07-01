Upgraded SARAI Interactive Maps Backend implemented using GEE API + Flask.

# Installation of Requirements
1. All Operating Systems
2. Python 3.6

## Ubuntu
1. Install Pip: `sudo apt-get install python3-pip`
2. Install VirtualENV: `pip3 install virtualenv`

## Running
1. Setup virtualenv for the project: `virtualenv venv`. Make sure this is executed inside the project root folder
2. Activate virtualenv by running: `source venv/bin/activate`
3. Install application requirements via:`pip3 install -r requirements.txt`. This will install all required dependencies of the application.
4. Add your Earth Engine credentials by modifiying `conf/main.yml`
5. Run the app by running the command: `python run.py`
