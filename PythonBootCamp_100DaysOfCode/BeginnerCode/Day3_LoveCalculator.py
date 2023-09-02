print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n ")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

t_count = name1.count('t') + name2.count('t')
r_count = name1.count('r') + name2.count('r')
u_count = name1.count('u') + name2.count('u')
e_count = name1.count('e') + name2.count('e')

l_count = name1.count('l') + name2.count('l')
o_count = name1.count('o') + name2.count('o')
v_count = name1.count('v') + name2.count('v')
e_count2 = name1.count('e') + name2.count('e')

left_num = str(t_count + r_count + u_count + e_count)
right_num = str(l_count + o_count + v_count + e_count2)

score = int(left_num + right_num)

if (score < 10 or score > 90):
    print(f"Your score is {score}, you go together like coke and mentos")
elif (score >= 40 and score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")
