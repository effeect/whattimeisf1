"""Class to grab to convert the race data into a html table format"""
class race_data:
    """Grabs the race data and converts it to a HTML table"""
    def __init__(self, data):
        """Initialize with race data and separate out the session information"""
        self.race_dataframe = data
        self.event_sessions = []
        for x in range(1, 6):
            session_info_date = data.get_session_date(x, utc="UTC-00:00")
            session_info_name = data.get_session_name(x)
            # Include the ID number as a separate attribute in the session data
            self.event_sessions.append({'id': x, 'name': session_info_name, 'date': session_info_date})
        
    def generate_table(self):
        """Generates a HTML table manually with data-id attributes"""
        table_data = '<tbody>\n'
        
        # Add each session as a row with a data-id attribute
        for session in self.event_sessions:
            table_data += f'    <tr>\n'
            table_data += f'      <td>{session["name"]}</td>\n'
            table_data += f'      <td data-id="time">{session["date"]}</td>\n'
            table_data += '    </tr>\n'
        
        # Close the tbody and table tags
        table_data += '  </tbody>'
        
        return table_data
        

# Uncomment below to test class

#if __name__ == "__main__":
#    test = race_data("hello world")
#    test.my_method("hello")