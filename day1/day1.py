import os

print("Current Working Directory:", os.getcwd())


with open('day1/day1.txt', 'r') as file:
    puzzle_input = file.readlines()

first_col = []
second_col = []

for line in puzzle_input:
    cols = line.split()
    first_col.append(cols[0])
    second_col.append(cols[1])

first_col.sort()
second_col.sort()
distance = 0
counter = 0

for i in range(len(first_col)):
    rel_dist = abs(int(first_col[i]) - int(second_col[i]))
    distance += rel_dist
    counter += 1

print(counter) #check that 1000 lines are checked
print(distance) #answer