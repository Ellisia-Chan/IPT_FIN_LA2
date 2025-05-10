# IPT_FIN_LA2

## 1. Setup Virtual Environment:
### Linux
sudo apt-get install python3-venv # If needed
python3 -m venv .venv
source .venv/bin/activate

### macOS
python3 -m venv .venv
source .venv/bin/activate

### Windows
py -m venv .venv
.venv\scripts\activate

## 2. Install Requirements:
pip install -r requirements.txt

## Running the Web Server:
In (venv)cmd, Select dir to fin_LA2\lab_problem
run: py manage.py runserver