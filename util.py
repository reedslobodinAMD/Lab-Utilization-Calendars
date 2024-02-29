from datetime import *
from dateutil.parser import *
from calendar_view.core.event import Event
import pytz

timeframe = 7
min_calendar_time_resolution = 531

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

def create_multi_day_event(title, start, end):
    event_list = []
    mid_start = start
    mid_end = mid_start.replace(hour=23,minute=59,second=59,microsecond=999)

    while mid_end.date() != end.date():
        timedelta = (mid_end-mid_start).total_seconds()
        if timedelta >= min_calendar_time_resolution:
            mid_event = Event(title=title, day=mid_start.date(), start=mid_start.time(), end=mid_end.time())
            event_list.append(mid_event)

        mid_start = mid_start.replace(day=mid_start.date().day+1, hour=0,minute=0,second=0,microsecond=1)
        mid_end = mid_start.replace(hour=23,minute=59,second=59,microsecond=999)

    mid_end = mid_end.replace(hour=end.time().hour,
                                minute = end.time().minute,
                                second = end.time().second,
                                microsecond = end.time().microsecond)
    timedelta = (mid_end-mid_start).total_seconds()
    if timedelta >= min_calendar_time_resolution:
        mid_event = Event(title=title, day=mid_start.date(), start=mid_start.time(), end=mid_end.time())
        event_list.append(mid_event)
    return event_list

def create_event(title, start, end):
    start = utc_to_pacific(start)
    end = utc_to_pacific(end)

    timedelta = (end-start).total_seconds()
    if timedelta < min_calendar_time_resolution:
        return None
    elif start.date() != end.date():
        return create_multi_day_event(title, start, end)
    return Event(title=title, day=start.date(), start=start.time(), end=end.time())

def timeframe_days_ago():
    now = datetime.now(timezone.utc)
    return now.replace(day=now.day - timeframe - 1)


def event_lists_add_event(event_lists, event, sut_name):
    if event == None:
        return

    #print(sut_name)
    #print("event start:" + str(event.start_time) + " event end: " + str(event.end_time))
    found = False
    for system_event_list in event_lists:
            if system_event_list.hostname == sut_name:
                system_event_list.addEvent(event)
                found = True

    if not found:
        system_event_list = SystemEventList(sut_name)
        system_event_list.addEvent(event)
        event_lists.append(system_event_list)
