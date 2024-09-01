from datetime import datetime

def convert_date_format(value):
    try:
        # Parse the date from DD-MM-YYYY format
        date_obj = datetime.strptime(value, '%d-%m-%Y')
        # Format the date as YYYY-MM-DD
        return date_obj.strftime('%Y-%m-%d')
    except ValueError:
        return "Invalid date format"

print(convert_date_format('01-09-2024'))