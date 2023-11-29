#!/usr/bin/python3
pairs = []
pairs.append("01")
for i in range(2, 10):
    for j in range(i+1, 10):
        pairs.append("".join(map(str, [i, j])))
print(", ".join(pairs))
