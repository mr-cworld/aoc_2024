#Day 1 Part 2
import os

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

sim_score = 0

for f_line in range(len(first_col)):
    instances = 0 
    for s_line in range(len(second_col)):
        if first_col[f_line] == second_col[s_line]:
            instances += 1 
    loop_res = instances * int(first_col[f_line])
    sim_score += int(loop_res) 

print(sim_score)
