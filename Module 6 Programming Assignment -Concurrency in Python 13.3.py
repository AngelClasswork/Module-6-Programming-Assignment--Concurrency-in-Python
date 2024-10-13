#13.3

from datetime import datetime
today_string = "2024-10-12" 

# Parse the date
parsed_date = datetime.strptime(today_string, "%Y-%m-%d")

print(parsed_date)
