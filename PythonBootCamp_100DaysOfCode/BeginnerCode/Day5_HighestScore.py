student_scores = input("Input a list of student scores: ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

highest = 0

for n in student_scores:
    if n > highest:
        highest = n

print(f"The highest score is: {highest}")
