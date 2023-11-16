import fastf1.events
from jinja2 import Template

import fastf1
import datetime
import pandas as pd


# https://docs.fastf1.dev/examples/index.html

# Thanks to https://stackoverflow.com/questions/32237862/find-the-closest-date-to-a-given-date
def nearest_event(items):
    """Getting the nearest next possible date"""
    return min(items, key=lambda x: abs(x - datetime.datetime.now()))

def publish_html(data):
    with open("index.html", "w") as file_:
        file_.write(data)
        file_.close()

if __name__ == "__main__":
    year = datetime.date.today().year

    schedule = fastf1.events.get_event_schedule(2023)
    # To look at all the possible data points
    # for column in schedule:
    #     print(schedule[column])
    date = nearest_event(schedule["EventDate"])
    next_date = schedule.loc[schedule['EventDate'] == f'{date}']

    prev_race = fastf1.get_event(year, next_date["RoundNumber"].values[0] - 1)
    race_data = fastf1.get_event(year, next_date["RoundNumber"].values[0])
    next_race = fastf1.get_event(year, next_date["RoundNumber"].values[0] + 1)

    print(prev_race)
    print(race_data)
    print(next_race)

    print(race_data[3])
    event_info = race_data[3]

    event_sessions = []
    # Organizes it into one array
    for x in range(1, 6):
        session_info_date = race_data.get_session_date(x, utc="UTC-00:00")
        session_info_name = race_data.get_session_name(x)
        event_sessions.append([session_info_name, session_info_date])
        print(session_info_name, session_info_date)

    with open('index_template.html') as file_:
        template = Template(file_.read())

    output = template.render(event=event_info,
                             session_1_name=event_sessions[0][0],
                             session_1_date=event_sessions[0][1],
                             session_2_name=event_sessions[1][0],
                             session_2_date=event_sessions[1][1],
                             session_3_name=event_sessions[2][0],
                             session_3_date=event_sessions[2][1],
                             session_4_name=event_sessions[3][0],
                             session_4_date=event_sessions[3][1],
                             session_5_name=event_sessions[4][0],
                             session_5_date=event_sessions[4][1]
                             )

    publish_html(output)
    # html_table = race_data.to_frame().to_html(classes='table table-bordered table-dark" id="myTable')
    # print(html_table)
