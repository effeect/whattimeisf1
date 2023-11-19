import fastf1
from tabulate import tabulate

class race_data:
    """Grabs the race data and convert it to a HTML table
    """
    # Define a constructor that takes one parameter and assigns it to an instance attribute
    def __init__(self, data):
        # Assign the parameter to an instance attribute named instance_attribute
        self.race_dataframe = data
        
        # Seperate out the data
        self.event_sessions = []
        for x in range(1, 6):
            self.session_info_date = data.get_session_date(x, utc="UTC-00:00")
            self.session_info_name = data.get_session_name(x)
            self.event_sessions.append([self.session_info_name, self.session_info_date])
        # Need to figure out a way to format this better
        
    def generate_table(self):
        """Generates a HTML table with tabulate
        """
        table = tabulate(self.event_sessions, tablefmt='html')
        tbody = table.replace("table","tbody")
        return(tbody)
        

# Uncomment below to test class

#if __name__ == "__main__":
#    test = race_data("hello world")
#    test.my_method("hello")