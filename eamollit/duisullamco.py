from datetime import datetime
import pytz

# Function to display local date and time in Eastern Time
def display_local_datetime_et():
    # Define the Eastern Timezone
    eastern = pytz.timezone('US/Eastern')
    
    # Get the current time in UTC
    utc_now = datetime.utcnow()
    
    # Convert UTC time to Eastern Time
    et_now = utc_now.astimezone(eastern)
    
    # Format the datetime object to the specified format
    formatted_datetime = et_now.strftime('%Y-%m-%d %I:%M:%S %p ET')
    
    return formatted_datetime

# Call the function and print the result
print(display_local_datetime_et())
