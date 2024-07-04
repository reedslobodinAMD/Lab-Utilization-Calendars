#!/bin/bash
#cd /home/isvperf/mi300x_h100_usage_tool
source env/bin/activate
source .env
#./trash_disposal.sh
env/bin/python3 main.py 
#./update_confluence.sh
cp html/* usage_webpage/usage_webpage/views/
