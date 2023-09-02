# 1 can of paint = 5 square meters
import math


def paint_calc(height, width, coverage):
    num_cans = math.ceil((height * width) / coverage)
    print(f"Number of cans needed: {num_cans}")


height = int(input("Height of wall (in meters): "))
width = int(input("Width of wall (in meters): "))
coverage = 5
paint_calc(height=height, width=width, coverage=coverage)
