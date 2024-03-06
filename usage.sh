#!/bin/bash
cd /home/isvperf/mi300x_h100_usage_tool
source env/bin/activate
source .env
env/bin/python3 main.py 
./update_confluence.sh
