import fastf1.events
from jinja2 import Template

import fastf1
import datetime
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

    schedule = fastf1.events.get_event_schedule(2024)
    # To look at all the possible data points
    # for column in schedule:
    #     print(schedule[column])
    date = nearest_event(schedule["EventDate"])
    print(date)
    next_date = schedule.loc[schedule['EventDate'] == f'{date}']

    race_data_class = fastf1.get_event(year, next_date["RoundNumber"].values[0])

    event_info = race_data_class[3]

    event_sessions = []
    current_race = race_data.race_data(race_data_class)
    table = current_race.generate_table()

    with open('index_template.html', encoding="UTF8") as file_:
        template = Template(file_.read())

    output = template.render(event=event_info,
                             table=table)

    publish_html(output)