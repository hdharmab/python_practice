conversion_val = 24
unit = "hours"


def days_to_seconds(num_days):
    return f"{num_days} days are {num_days * conversion_val} {unit}"


def validate_and_execute(user_input_element):
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
        # we can also have except: to catch all errors
        except ValueError:
            print(f"You entered {user_input_element}, Enter a positive integer!")


user_input_message = "Enter the number of days to convert to hours or type exit :\n"

