import random

names_string = input(
    "Give me a list of everyone's name, separated by comma: \n")

nameList = names_string.split(",")
idx = random.randint(0, len(nameList)-1)

print(f"{nameList[idx]} is going to buy the meal today!")
