"""
This program calculates the time remaining for a deadline
"""
import datetime

user_input = input("Enter you goal with a deadline separated by a colon\n")
input_list = user_input.split(":")

goal_variable = input_list[0]
deadline = input_list[1]
deadline = deadline.strip() # remove whitespaces as white spaces are not accepted by strptime()
deadline_date = datetime.datetime.strptime(deadline,"%d.%m.%Y")

# today's datetime
current_datetime = datetime.datetime.today()

# calculate the number of days from today to the deadline
time_remaining = deadline_date - current_datetime
time_days = time_remaining.days
time_seconds = time_remaining.total_seconds()
time_hours = time_remaining.total_seconds()/3600

# print a message to the user
# print(f"Dear user, time remaining for your goal: {goal_variable} is {time_remaining}\n"
#       f" or {time_days} days \n or {time_seconds} seconds\n  or {time_hours} hours\n ")

# print(f"The remaining time to complete your goal {goal_variable} is: \n"
#       f"days: {time_remaining.days}\n"
#       f"Hours: {int(time_hours)}")

print(f"The remaining time to complete your goal {goal_variable} is {time_remaining}\n")
print(f"The remaining time to complete your goal {goal_variable} is {time_remaining}\n")



