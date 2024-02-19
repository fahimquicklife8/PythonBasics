#arrays are called lists in python
array = [1,2,3]
print(array)

#Can be used as a stack
array.append(4)
array.append(5)
print(array)

array.pop()   #pops the last value
print (array)

array.insert(1,7)   #inserts 7 into index of 1
print(array)
array[0] = 0
array[3] = 0
print(array)

#read last value & sublist
print(array[-1])
print(array[1:3])
print(array[0:4])

a,b , c= [1,2,3]
print(a,b,c)

# for loops below
nums = [1,3,2,4,5,6]
for n in nums:
    print(n)

for i in range(len(nums)):
    print(nums[i])

for i, n in enumerate(nums):    #prints index and the item in array/list
    print(i,n)

num1 = [1,2,3]
num2 = [4,5,6]
for n1, n2 in zip(num1, num2):
    print(n1,n2)

num1.reverse()