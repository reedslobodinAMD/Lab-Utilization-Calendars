from datetime import *
from dateutil.parser import *
from calendar_view.core.event import Event
from calendar_view.core.event import EventStyles

import pytz

timeframe = 7
#540
min_calendar_time_resolution = 530

class SystemEventList:

    def __init__(self, hostname):
        self.hostname = hostname
        self.events = []

    def addEvent(self, events):
        if isinstance(events, Event):
            self.events.append(events)
        else:
            for event in events:
                self.events.append(event)

def utc_to_pacific(utc_datetime):
    return utc_datetime.replace(tzinfo=timezone.utc).astimezone(pytz.timezone('US/Pacific'))

def create_multi_day_event(title, start, end, event_lists, sut_name, style):
    mid_end = start.replace(hour=23,minute=59,second=59,microsecond=999000)

    #print("start: " + str(start) + "    mid end: " + str(mid_end))
    #print("mid start: " + str(mid_end+timedelta(milliseconds=2)) + "    end: " + str(end))

    create_event(title, start, mid_end, event_lists, sut_name, style)
    create_event(title, mid_end+timedelta(milliseconds=2), end, event_lists, sut_name, style)


def create_event(title, start, end, event_lists, sut_name, style):
    
    timedelta = (end-start).total_seconds()
    if timedelta < min_calendar_time_resolution:
        return
    
    if(sut_name == "ppac-1e707-a03-1.mkm.dcgpu"):
        print("\n\ngotem\n\n")

    elif start.date() != end.date():
        create_multi_day_event(title, start, end, event_lists, sut_name, style)
        return
    event = Event(title=title, day=start.date(), start=start.time(), end=end.time(), style=style)
    event_lists_add_event(event_lists, event, sut_name)

def timeframe_days_ago():
    now = datetime.now(timezone.utc)
    return now - timedelta(days=(timeframe))


def event_lists_add_event(event_lists, event, sut_name):
    if event == None:
        print("\n\n\n\nLSADJLSKDJFKLSJDFLKJSDKLFJLKSDJF\n\n\n\n")
        return


    sut_name=sut_name.split('.')[0]

    if(sut_name == "ppac-1e707-a03-1"):
        print("\n\n\nNOW HERE\n\n\n")

    #print(sut_name)
    #print("event start:" + str(event.start_time) + " event end: " + str(event.end_time))
    for system_event_list in event_lists:
        if system_event_list.hostname == sut_name:
            system_event_list.addEvent(event)
            return

    system_event_list = SystemEventList(sut_name)
    system_event_list.addEvent(event)
    event_lists.append(system_event_list)
