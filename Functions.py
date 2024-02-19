#Functions in python
def Prime(n):
    for i in range (2,n):
        if(n%i == 0):
            return False
    return True

for i in range(2,100):        #prime number
    if Prime(i):
        print(i)


#functions do not have to be explicitly declared
def myFunction(n,m):
    print(n*m)
myFunction(3,4)

#means that same function can be used with or without return statement as shown below
def myFunction(n,m):
    return(n*m)
print(myFunction(3,4))

