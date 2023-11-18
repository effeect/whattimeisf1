import fastf1

class race_data:
    # Define a class attribute that is shared by all instances of the class

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
        # print(session_info_name, session_info_date)
        
        print(self.event_sessions)
        # Need to figure out a way to format this better
        self.session_1_name = "placeholder1"
        self.session_1_time = "placeholder1"
        self.session_2_name = "placeholder2"
        self.session_2_time = "placeholder2"
        self.session_3_name = "placeholder3"
        self.session_3_time = "placeholder3"
        self.session_4_name = "placeholder4"
        self.session_4_time = "placeholder4"
        self.session_5_name = "placeholder5"
        self.session_5_time = "placeholder5"
        

    # Define a method that takes one parameter and returns the sum of the instance attribute and the parameter
    def my_method(self, parameter):
        # Return the sum of the instance attribute and the parameter
        print(self.race_dataframe)

# Uncomment below to test class

#if __name__ == "__main__":
#    test = race_data("hello world")
#    test.my_method("hello")