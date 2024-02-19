# in sets values can exist only once, so no duplicates
mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet)   #prints entire set
print(len(mySet))     #prints length of set

print(1 in mySet)   #check if 1 exists in the set
print(2 in mySet)   #check if 2 exists in the set
print(3 in mySet)

mySet.remove(2)       #removes value from set
mySet.remove(1)
print(mySet)

#initiliaze hashset with a bunch of values
print(set([1,2,3]))
mySet = {i for i in range(5)}
print(mySet)