"""
This program converts days to hours
Supplementary File: helper.py
"""
from re import split
from helper import validate_and_execute, user_input_message
# or import all using: from helper import *

user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    user_days = split('[,; 	]', user_input)
    days = sorted(set(filter(None, user_days)))
    for user_input_element in days:
        validate_and_execute(user_input_element)
