#!/bin/bash
# build_files.sh
pip install -r requirements.txt
python3.9.6 manage.py collectstatic

