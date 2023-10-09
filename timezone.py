import pyperclip
from dateutil import parser, tz
from datetime import datetime

def convert_timezone(time_input):
    # Determine the timezone from the input
    input_tz = None
    if 'PDT' in time_input.upper():
        input_tz = tz.gettz('America/Los_Angeles')
        time_input = time_input.replace('PDT', '').strip()
    elif 'UTC' in time_input.upper():
        input_tz = tz.tzutc()
        time_input = time_input.replace('UTC', '').strip()
    elif 'AEST' in time_input.upper():
        input_tz = tz.gettz('Australia/Sydney')
        time_input = time_input.replace('AEST', '').strip()
    
    # Parse the time input
    if len(time_input.split()) == 1:  # Only time is provided
        today_date = datetime.now().strftime('%Y-%m-%d')
        input_time = parser.parse(f'{today_date} {time_input}')
    else:  # Time and date are provided
        input_time = parser.parse(time_input)
    
    input_time = input_time.replace(tzinfo=input_tz)
    
    # Convert to other timezones
    utc_time = input_time.astimezone(tz.tzutc())
    pdt_time = input_time.astimezone(tz.gettz('America/Los_Angeles'))
    aest_time = input_time.astimezone(tz.gettz('Australia/Sydney'))
    
    result = (
        f'UTC {utc_time.strftime("%Y-%m-%dT%H:%M:%S")}, '
        f'PDT {pdt_time.strftime("%Y-%m-%dT%H:%M:%S")}, '
        f'AEST {aest_time.strftime("%Y-%m-%dT%H:%M:%S")}'
    )

    print(result)
    pyperclip.copy(result)

if __name__ == '__main__':
    time_input = input("Enter a time with or without a date, and a timezone (UTC, PDT, AEST): ")
    convert_timezone(time_input)
