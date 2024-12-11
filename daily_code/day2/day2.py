import os

with open('daily_code/day2/puzzle_input.txt', 'r') as file:
    puzzle_input = file.readlines()

safe_reports = 0 #answer

for line in puzzle_input:
    entries = line.strip().split()

    numbers = list(map(int, entries))

    is_increasing = None
    is_safe = True

    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]

        if not(1<= abs(diff) <= 3):
            is_safe = False
            break
        
        if is_increasing is None:
            if diff > 0:
                is_increasing = True
            elif diff < 0:
                is_increasing = False
            else:
                is_safe = False
                break
        
        else: 
            if is_increasing and diff <=0:
                is_safe = False
                break
            
            if not is_increasing and diff >= 0:
                is_safe = False
                break
    if is_safe:
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
'''
