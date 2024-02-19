
#sorting is very easy in python

arr = [3,7,5,9,0,5,6,8,3]
arr.sort()
print(arr)

#strings get sorted by what letter they start
string = ["Penis", "Boobs", "Dick", "Cock"]
string.sort()
print(string)

# but if we want to sort by length of string

string.sort(key=lambda x: len(x))
print(string)





