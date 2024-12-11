import os

with open('daily_code/day2/puzzle_input.txt', 'r') as file:
    puzzle_input = file.readlines()

safe_reports = 0 #answer

def is_safe_seq(sequence):
    if len(sequence) < 2:
        return True #base case, 1 number always okay
    is_increasing = None
    for i in range(len(sequence)-1):
        diff = sequence[i+1] - sequence[i]
        if not (1 <= abs(diff) <= 3):
            return False
        if is_increasing is None:
            if diff > 0:
                is_increasing = True
            elif diff < 0:
                is_increasing = False
        else:
            if is_increasing and diff <= 0:
                return False
            if not is_increasing and diff >=0:
                return False
    return True


for line in puzzle_input:
    entries = line.strip().split()

    numbers = list(map(int, entries))
    n = len(numbers)

    if is_safe_seq(numbers):
        safe_reports += 1
        continue

    #if not safe, remove one elemenat at each position and check
    made_safe = False
    for i in range(n):
        mod_seq = numbers[:i] + numbers[i+1:]
        if is_safe_seq(mod_seq):
            made_safe = True
            break

    if made_safe:
        safe_reports += 1

print(safe_reports)
         


''' Example Output from entries.split / len
['78', '81', '83', '85', '88']
5
['11', '10', '7', '4', '2']
5
['43', '46', '48', '50', '52', '54']
6
['12', '14', '15', '16', '17', '18', '19', '21']
8

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.

First attempt - 5199, too high
Second attempt - 3629, too high
Third - 606, correct

Part 2
First - 644 - correct
'''
