#!/usr/bin/python3
numbers = []

for i in range(0, 100):
    numbers.append('{:02d}'.format(i))

print(', '.join(numbers))
