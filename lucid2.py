from util import *
import requests
import json

base_url = "https://lucid.amd.com/api/v1/"

def get_mi300_hosts():
    mi300a_hosts = ""
    mi300x_hosts = ""

    with open("mi300a_hosts.txt", "r") as filestream:
        for line in filestream:
            mi300a_hosts = mi300a_hosts + line.split()[0] + ","

    with open("mi300x_hosts.txt", "r") as filestream:
        for line in filestream:
            mi300x_hosts = mi300x_hosts + line.split()[0] + ","

    return mi300a_hosts + mi300x_hosts

def parse_lucid2_job(job):
    title = job["run_label"]

    for message in job["conductor_metadata"]["metadata"]:
        if "callback" not in message:
            continue
        data = eval(job["conductor_metadata"]["metadata"][message].replace("'", '"'))

        if "date_time_end" in data and data["date_time_end"] != None:
            start = parse(data["date_time_start"])
            end = parse(data["date_time_end"])
            return create_event(title, start, end)

    return None

""""Get list of MI300 Jobs in past week from Lucid2"""

def get_lucid2_job_events(event_lists):
    hosts = get_mi300_hosts()
    job_url = base_url + "job" + \
                    "?sut_names=" + hosts + \
                    "&created_after=" + str(timeframe_days_ago()) +\
                    "&count=1000"
    print(job_url)

    search = requests.get(job_url, verify=False)

    results_json = search.json()["results"]

    for job in results_json:
        sut_name = job["conductor_metadata"]["sut_names"][0]
        event = parse_lucid2_job(job)
        event_lists_add_event(event_lists, event, sut_name)

