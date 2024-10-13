# Import the ability for the program to call the date.
from datetime import datetime

# Get the current date. use the strftime to format the date. 
current_date = datetime.now().strftime("%m-%d-%Y")

# Write the current date to a text file. The text file will be called 'today.txt'
with open("today.txt", "w") as file:
    file.write(current_date)

#13.2 
#Read the text file today.txt into the string today_string
with open("today.txt", "r") as file:
    today_string = file.read()

print(today_string)

#13.3

from datetime import datetime
today_string = "2024-10-12" 

# Parse the date
parsed_date = datetime.strptime(today_string, "%Y-%m-%d")

print(parsed_date)
