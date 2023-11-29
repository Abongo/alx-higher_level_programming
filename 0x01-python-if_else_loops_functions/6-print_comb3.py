#!/usr/bin/python3
def generate_pairs():
    for i in range(10):
        for j in range(i + 1, 10):
            if j != i:
                yield "{}{},".format(i, j)


pairs = list(generate_pairs())
# remove the last comma from the last element
pairs[-1] = pairs[-1].rstrip(',')
# print all the pairs separated by an empty space
print(' '.join(pairs))
