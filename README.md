# IPT_FIN_LA2

## 1. Setup Virtual Environment:
### Linux
sudo apt-get install python3-venv # If needed </br>
python3 -m venv .venv </br>
source .venv/bin/activate

### macOS
python3 -m venv .venv </br>
source .venv/bin/activate

### Windows
py -m venv .venv </br>
.venv\scripts\activate

## 2. Install Requirements:
pip install -r requirements.txt

## Running the Web Server:
In (venv)cmd, Select dir to fin_LA2\lab_problem </br>
run: py manage.py runserver