#! /bin/sh
python3.6 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
cd ./dumbpy/
make
cd ../
make
