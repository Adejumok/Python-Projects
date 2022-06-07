# for i in range(1, 13):
#     for j in range(1, 13):
#         print("{:4d} * {:>2d} ={:>4}".format(i, j, i * j))
#     print()

import itertools

for i, j in itertools.product(range(1, 13), range(1, 13)):
    print("{:4d} * {:>2d} ={:>4}".format(i, j, i * j))
    if j == 12:
        print()

