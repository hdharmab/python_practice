
import re

conversion_val = 24
unit = "hours"


def days_to_seconds(num_days):
	return f"{num_days} days are {num_days*conversion_val} {unit}"


def validate_and_execute():
	if user_input_element == "exit":
		print("You have exited the program!")
	else:
		try:
			user_input_num = int(user_input_element)
			# check for positives and 0's
			if user_input_num > 0:
				my_var = days_to_seconds(user_input_num)
				print(my_var)
			elif user_input_num == 0:
				print("You entered 0 days, no conversion for you")
			else:
				print(f"You entered {user_input_num}, a negative number!")	
		except ValueError:
			print(f"You entered {user_input_element}, Enter a positive integer!")


user_input = ""
while user_input != "exit":
	user_input = input("Enter the number of days to convert to hours or type exit :\n")
	user_days = re.split('[,; 	]', user_input)
	days = list(filter(None, user_days))
	# print(days)
	for user_input_element in days:
		validate_and_execute()
