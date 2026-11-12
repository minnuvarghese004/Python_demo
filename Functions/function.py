#Functions are block of reusable code where logic will be defined in the parent module
# and execution can be performed in any one of the child modules

#function syntax
#def function_name():  - definition or declaration function
    #block of codes
#function_name()  -calling or invocation of function

#Write a python function to print "hello world"
# def message():
#     print("hello world")
#
# #print("Hi")
# message()

#Type of functions-parameterized and non parameterized (without passing any external values)
#parameters - variables used to receive the values - in def
# def greeting(name):  #parameter list
#     print(f"hello dear {name}")
# greeting("Minnu")  # minnu will store in name
# greeting("ABC")
#the value passed through invocation is called as argument
#the variable that stores the argument is called as parameter
#this together is called as a parameterized function

#type of parameters/arguments
#all data types
# def student(name,age,place,contact):
#     print(f"{name}-{age}-{place}-{contact}")
# student("Minnu",20,"Cochin",[1234,5678])

#Default parameters
# def student(name,age,place,contact,grade="5th"):
#     print(f"{name}-{age}-{place}-{contact}-{grade}")
# student("Minnu",20,"Cochin",[1234,5678])
# student("Chinnu",30,"Tvm",[7890,3456],"6th")

#arbitrary arguments (*args)
# def details(*data):   #* = converts into tuple and lets you pass any number of positional arguments and store in tuple,method to accept multiple arguments
#     print(data)
#     # print(type(data))   -tuple
# details("Minnu",20,"Cochin",[1234,5678])

#keyword arguments  - specify the parameter name when passing a value (in invocation line)
# def details(age,name,location="Tvm"):
#     print(name,age,location)
# details(name="Arjun",age=25)

#Arbitrary keyword  arguments -(**kwargs) - to accept any number of keyword arguments.
# def details(**data):   # collects keyword arguments into a dictionary
#     print(data)
#     print(type(data))   #dictionary
# details(name="Arjun",age=25)
# details(name="Ajay",age=30,place="Ktm")

#return statement
# def addition(a,b):
#     #print(a+b)
#     return a*b  # returns 2*5 =10 to invocation line variable (x=10),
#     # sends the result back to the place where the function was called.
#                 # immediately stops the function
#
# x=addition(2,5)
# print(x)

#scope of a variable - means the area of a program where a variable can be accessed or used
#Two types os scope - Local scope and Global scope
#Local variable - it's a variable declared inside a function, can be accessed only inside the function
# def show():
#     name="Minnu"
#     print(name)
# show()
# print(name)  # name is not defined enrror

#Global Variable - It is declared outside all functions and can be accessed both inside and outside functions
# name="Minnu"
# print(name)
# def show():
#     name ="Arjun"
#     print(name)
# show()
# print(name)

#using global keyword, we can modify the scope of a locally declared variable
# name="Minnu"
# print(name)
# def show():
#     global name,x
#     name ="Arjun"
#     print(name)
#     x=20
# show()
# print(name)
# print(x)


