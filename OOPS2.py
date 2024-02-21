class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("Fahim")
print(s1.name)


#now we will talk about private attribute
#usually classes are public but
#This is actually public which is a problem
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass

acc1 = Account("12345", "abcde")
print(acc1.acc_no, acc1.acc_pass)

#Lets try to make a private function

class Person:
    __name = "anonymous"

    def __hello(self):
        print("Hello Person!")
    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome())

# check below car example
class Car:
    color = "black"
    @staticmethod
    def start():
        print("Car Started Vroom vroom...")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name


car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.start())
print(car1.color)

#Again one more example of classes and objects

class Vehicle:

    def __init__(self, make, model):      #here init is a method inside car class
        self.make = make
        self.model = model
    def drive(self):
        print(f"{self.make} {self.model} is driving")

    def highway_jump(self):
        print(f"{self.make} {self.model} jumped off highway")
class ToyotaCar(Vehicle):
    def __init__(self, name, drive):
        super().__init__(drive)
        self.name = name




car1 = Vehicle("Honda", "Civic")         #objects are being created
car2 = Vehicle("Toyota", "corolla")      #objects that pass parameter
car1.highway_jump()
car2.highway_jump()                                #drive method gets called by car object

car1.drive()



