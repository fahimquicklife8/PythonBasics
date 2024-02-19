#Division is decimal by default
print(5/2)
#Double slash rounds down
print(5 // 2)
#Careful: msot languages round towards 0 by default
#so negative numbers round down
print(-3 // 2)
#A work around for rounding towars zero is to
# use decimal division and then convert to int
print(int(-3/2))
# Using modula operator
print(10%3)
#using modulo opertor in negative
print(-10%3)

import math
print(math.fmod(-10,3))

#More math helpers
print(math.floor(3/2))
print(math.ceil(3/2))
print(math.pow(2,3))
print(math.sqrt(256))

#max integer
print(float("inf"))
#min Integer
print(float("-inf"))
# example of very large integer
print(math.pow(2,200))
#But still less than infinity
print((math.pow(2,200))< float("inf"))







