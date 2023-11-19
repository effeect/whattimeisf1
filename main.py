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
    return min(items, key=lambda x: abs(x - datetime.datetime.now()))

def publish_html(data):
    """Writes a index.html file"""
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
    race_data_class = fastf1.get_event(year, next_date["RoundNumber"].values[0])
    next_race = fastf1.get_event(year, next_date["RoundNumber"].values[0] + 1)

    event_info = race_data_class[3]

    event_sessions = []
    current_race = race_data.race_data(race_data_class)
    table = current_race.generate_table()

    with open('index_template.html', encoding="UTF8") as file_:
        template = Template(file_.read())

    output = template.render(event=event_info,
                             table=table)

    publish_html(output)
    # html_table = race_data.to_frame().to_html(classes='table table-bordered table-dark" id="myTable')
    # print(html_table)
