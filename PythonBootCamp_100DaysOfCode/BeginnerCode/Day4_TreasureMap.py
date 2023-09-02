row1 = ["", "", ""]
row2 = ["", "", ""]
row3 = ["", "", ""]
grid = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want to put the treasure?")

col = int(position[0])-1
row = int(position[1])-1

grid[row][col] = "X"
for i in grid:
    print(i)
