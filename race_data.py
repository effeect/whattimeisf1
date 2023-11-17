import fastf1

class race_data:
    # Define a class attribute that is shared by all instances of the class
    class_attribute = "This is a class attribute"

    # Define a constructor that takes one parameter and assigns it to an instance attribute
    def __init__(self, dataframe):
        # Assign the parameter to an instance attribute named instance_attribute
        self.race_dataframe = dataframe

    # Define a method that takes one parameter and returns the sum of the instance attribute and the parameter
    def my_method(self, parameter):
        # Return the sum of the instance attribute and the parameter
        print(self.race_dataframe)
        return self.instance_attribute + parameter