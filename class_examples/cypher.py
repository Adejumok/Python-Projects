# for p in "python":
#     print(p, end='')

import string

abc = string.ascii_lowercase
g = "hello"
key = 5
trans = abc[key:] + abc[:key]
cypher = g.translate(str.maketrans(abc, trans))
print(cypher)
print()
print(cypher.translate(str.maketrans(trans, abc)))
