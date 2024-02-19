#HashMap is the most used datastructure

myMap = {}
myMap["Alica"] = 88
myMap["bob"] = 77
print(myMap)
print(len(myMap))

myMap["alice"] = 80
print(myMap["alice"])

#hasmaps are basically called dictionaries in python

myMap = {i: i*2 for i in range(3) }
print(myMap)

for key in myMap:
    print(key,myMap[key])    #prints key and value regarding that key

for val in myMap.values():   #iterate through list of values in hashMap
    print(val)

for key, val in myMap.items():
    print(key,val)