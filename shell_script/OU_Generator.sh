#!/bin/bash
source ~/.virtualenvs/cv/bin/activate
python3 OU_Generator.py $1 $2 $3 
deactivate
