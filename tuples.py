#tuples are like arrays but immutable
tup = (1,2,3)
print(tup[0])

# mainly use tuples to pair keys with values in hashmap

myMap = { (1,2,3): 3}
print(myMap[(1,2,3)])

mySet = set()
mySet.add((1,2,3))         #add tuple to hashset
print((1,2,3) in mySet)

#lists or arrays cannot be keys so tuples are used




