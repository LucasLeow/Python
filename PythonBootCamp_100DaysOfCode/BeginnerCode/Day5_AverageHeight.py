student_heights = [180, 174, 165, 173, 189, 169, 159]
sum = 0
for height in student_heights:
    sum += height

print(f"Average Height: {round(sum / len(student_heights),2)}")
