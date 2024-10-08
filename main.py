from lucid2 import *
from conductor import *
from create_calendar import *
from calendar_view.calendar import Calendar
from calendar_view.core.config import CalendarConfig
from calendar_view.config import style

hour_height = 200
'''
def create_calendar(system_event_list):
    style.hour_height = hour_height
    style.event_title_font = style.image_font(50)
    now = datetime.now(pytz.timezone('US/Pacific'))
    timeframe_days_ago = str((now - timedelta(days=timeframe)).date())
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
    if(hostname == "ppac-1e707-a03-1.mkm.dcgpu"):
        print("\n\nAKFHAKSJHFJKALSHF\n\n")
    #print(hostname) 
    #for event in system_event_list.events:
        #print(event.title)
        #print("start: " + str(event.start_time) + "      end: " + str(event.end_time))
        #delta = datetime.strptime(str(event.end_time), "%H:%M:%S") - datetime.strptime(str(event.start_time), "%H:%M:%S")
        #print("timedelta: " + str(delta.total_seconds()))
    

    calendar = Calendar.build(config)
    calendar.add_events(system_event_list.events)
    calendar.save( "images/" + hostname + "/" + hostname + "_usage_" + now + ".png" )
'''
def main():
    event_lists = {}
    get_conductor_reservation_events(event_lists)
    get_lucid2_job_events(event_lists)
    for sut_name, system_event_list in event_lists.items():
        plotly_calendar(sut_name, system_event_list)

"""
TODO:

    Pull additional data from other sources:
        Tower jobs?
        Conductor Batch Jobs
"""


if __name__ == '__main__':
    main()


