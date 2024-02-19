"""This file is designed to be executed in GitHub Actions to generate the index.html that gets displayed"""
import datetime
import fastf1.events
from jinja2 import Template

import fastf1
import pandas as pd
import race_data


# https://docs.fastf1.dev/examples/index.html

# Thanks to https://stackoverflow.com/questions/32237862/find-the-closest-date-to-a-given-date
def nearest_event(items):
    """Getting the nearest next possible date"""
    now = datetime.datetime.now()
    future_dates = [date for date in items if date > now]
    return min(future_dates, key=lambda x: abs(x - now))

def publish_html(data):
    """Writes a index.html file"""
    with open("index.html", "w") as file_:
        file_.write(data)
        file_.close()

if __name__ == "__main__":
    year = datetime.date.today().year

    schedule = fastf1.events.get_event_schedule(year)
    date = nearest_event(schedule["EventDate"])
    next_date = schedule.loc[schedule['EventDate'] == f'{date}']

    if(next_date["RoundNumber"].values[0] == 0):
        next_date["RoundNumber"].values[0] = 1 
        
    print(next_date["RoundNumber"].values[0])
    race_data_class = fastf1.get_event(year, next_date["RoundNumber"].values[0])

    # Taking the values from the Race Data class and formatting it
    # print(race_data_class)
    event_info = race_data_class.iloc[5]
    con_info = race_data_class.iloc[1]
    loc_info = race_data_class.iloc[2]

    event_sessions = []
    current_race = race_data.race_data(race_data_class)
    table = current_race.generate_table()

    with open('index_template.html', encoding="UTF8") as file_:
        template = Template(file_.read())

    output = template.render(event=event_info,
                             table=table,
                             country=con_info,
                             location=loc_info)

    publish_html(output)
