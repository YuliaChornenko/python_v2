"""
    Написати валідатор ....
    Правило валідації
"""

import re

def getStudent():

    user_input = input("Enter student:\n")

    if (re.match(r"^[A-Z]{2}\-\d{8}$", user_input) ):
        return user_input
    else:
        return False


"""
    Написати валідатор ....
    Правило валідації
"""

def getCompany():
    user_input = input("Enter company:\n")

    if (re.match(r"^[a-z]+\d{0,2}$", user_input)):
        return user_input
    else:
        return False



"""
    Написати валідатор ....
    Правило валідації
"""


def getSkill():
    user_input = input("Enter skill:\n")

    if (re.match(r"(^[a-z]+",user_input)):
        return user_input
    else:
        return False
