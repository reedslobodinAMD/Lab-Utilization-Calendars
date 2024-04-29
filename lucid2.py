from util import *
import requests
import json

base_url = "https://lucid.amd.com/api/v1/"

def get_lucid_hosts():
    mi300a_hosts = ""
    mi300x_hosts = ""
    h100_hosts = ""

    with open("mi300a_hosts.txt", "r") as filestream:
        for line in filestream:
            mi300a_hosts = mi300a_hosts + line.split()[0] + ","

    with open("mi300x_hosts.txt", "r") as filestream:
        for line in filestream:
            mi300x_hosts = mi300x_hosts + line.split()[0] + ","

    with open("h100_hosts.txt", "r") as filestream:
        for line in filestream:
            h100_hosts = h100_hosts + line.split()[0] + ","

    return mi300a_hosts + mi300x_hosts + h100_hosts

def parse_lucid2_job(job, event_lists, sut_name):
    title = job["run_label"]

    for message in job["conductor_metadata"]["metadata"]:
        if "callback" not in message:
            continue
        data = eval(job["conductor_metadata"]["metadata"][message].replace("'", '"'))

        if "date_time_end" in data and data["date_time_end"] != None:
            start = utc_to_pacific(parse(data["date_time_start"]))
            end = utc_to_pacific(parse(data["date_time_end"]))
            create_event(title, start, end, event_lists, sut_name, EventStyles.BLUE)

""""Get list of Jobs in past week from Lucid2"""

def get_lucid2_job_events(event_lists):
    hosts = get_lucid_hosts()
    job_url = base_url + "job" + \
                    "?sut_names=" + hosts + \
                    "&created_after=" + str(timeframe_days_ago()) +\
                    "&count=1000"
    #print(job_url)

    search = requests.get(job_url, verify=False)

    results_json = search.json()["results"]

    for job in results_json:
        sut_name = job["conductor_metadata"]["sut_names"][0]
        parse_lucid2_job(job, event_lists, sut_name)

