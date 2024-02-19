#list comprehension
arr = [i+i for i in range(5)]
print(arr)

#lists within lists hehe
arr = [[0]*4 for i in range(4)]
print(arr)
#but below we're not creating 4 different rows
arr = [[0]*4] * 4
print(arr)
