from lucid2 import *
from conductor import *
from calendar_view.calendar import Calendar
from calendar_view.core.config import CalendarConfig
from calendar_view.config import style

hour_height = 200

def create_calendar(system_event_list):
    style.hour_height = hour_height

    now = datetime.now(pytz.timezone('US/Pacific'))
    timeframe_days_ago = str(now.replace(day=now.day - timeframe).date())
    now = str(now.date())
    hostname = system_event_list.hostname
    config = CalendarConfig(
        lang='en',
        title="Past Week Usage for " + hostname,
        dates=timeframe_days_ago + " - " + now,
        hours='0 - 24',
        mode=None,
        show_date=True,
        show_year=False,
        legend=False,
    )
    
    for event in system_event_list.events:
        print(event.title)
        print("start: " + str(event.start_time) + "      end: " + str(event.end_time))
        #delta = datetime.strptime(str(event.end_time), "%H:%M:%S") - datetime.strptime(str(event.start_time), "%H:%M:%S")
        #print("timedelta: " + str(delta.total_seconds()))
    

    calendar = Calendar.build(config)
    calendar.add_events(system_event_list.events)
    calendar.save( hostname + "_usage_" + now + ".png" )

def main():
    event_lists = []
    #get_lucid2_job_events(event_lists)
    get_lucid2_job_events(event_lists)
    for system_event_list in event_lists:
        create_calendar(system_event_list)

"""
TODO:

    Pull additional data from other sources:
        Tower jobs?
        Conductor Batch Jobs
"""


if __name__ == '__main__':
    main()


