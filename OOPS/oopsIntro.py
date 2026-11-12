#OOPS(Object oriented programming language)
#It's a programming approach in which we organize our code using classes and objects
#Real world example
# A car category has properties (Brand ,color, model,speed) and has behaviours(start,stop,accelerate,brake)
#Each car object(Swift,BMW) under the category can have its own properties and behaviours
#In real oops programming, properties are represented using attributes
#Behaviours are represented using methods (Functions inside OOPS class)
#Objects are instances of class
#Class is the blueprint of objects
#Terms in OOPS-class,object,attributes,methods
#Advantages
#1.code reusability
#2.Code maintainability  -
#3.Encapsulating data and methods  - hold as single unit
#4.organizing entire code script

class CarClass:             #Creating class
    color="Black"           # defining attributes
    model="electric"

    def start(self):
        print("Engine started")

    def stop(self,distance):
        self.distance=distance                 #Instance variable is created,to use in other methods inside the class#
                                            # distance value is assigned to a self.distance variable
        print(f"car stopped at {distance}")   #variable can be distance or self.distance

    def detail(self):
        print(f"The car started and stopped at {self.distance} kms")      #if 2 methods are invoked by a single object,
                                                                    # then self.distnce can be reused


car1=CarClass()             # Creating objects
#print(color)               #not defined because cannot access variables inside the class directly,only objects can access the attributes
print(car1.color)

car2=CarClass()
print(car2.model)           #Any object can use the attributes inside the class

car1.speed="100Km/hr"       #New attribute creation..created the speed attribute only for car1. and saved inside the class
print(car1.speed)           #car1 has access to speed
#print(car2.speed)           # car2 cannot access speed as speed attribute is created by car1

car1.start()                # method can be invoked using object, mention in the func -using which object we invoked the function
#if we pass car1 to the function inside the class, the function can be used by only car1. not by other objects
#To refer the current object, we use 'Self' in the parameter of function
#If we design a method inside the class, first parameter should be self

#Self refers to the current object using which we invoke the method (self= car1, self=car2)
car2.start()      #self = car2

car1.stop(10)      #parameterized
#car2.stop(20)      #Different objects can pass different arguments inside a method
car1.detail()      #self=car1---- the value passed in a method of a class can be used by other methods. so need to pass an argument here
#In this case, the value 10 is reused inside detail() method ,this is possible because both stop and detail are invoked using
#same object(car1)
car2.stop(50)
car2.detail()

