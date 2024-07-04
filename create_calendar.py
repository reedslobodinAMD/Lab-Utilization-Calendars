import plotly.express as px
import pandas as pd
from calendar_view.core.event import Event


def plotly_calendar(sut_name, system_event_list):
    #print(sut_name)
    #print(system_event_list)

    df = pd.DataFrame(system_event_list)
    #for Event in system_event_list.events:
      #  df.update(dict(Task=Event.title, Start=Event.start_time, Finish=Event.end_time))
    print(sut_name)
    print(df)


    fig = px.timeline(df, 
            x_start="Start", 
            x_end="End", 
            y="Event_Type", 
            title = "Past Week Usage for " + sut_name,
            color = "Event_Type",
            text = "Task",
            hover_name = "Task")
    fig.update_yaxes(autorange="reversed")
    fig.write_html("./html/plotly_" + sut_name + ".html")
