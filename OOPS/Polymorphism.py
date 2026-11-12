#Polymorphism means one name with many forms
#It allows same method name (function) or operator to behave differently depending on the object
#The built-in polymorphic operator in python is '+' (for numbers, it performs addition and for string it performs concatenation)
# class Parent:
#     def skill(self):
#         print("Teaching skill")
#
# class Child1(Parent):
#     def skill(self):
#         super().skill()
#         print("Singing skill")
#
# class Child2(Parent):
#     def skill(self):
#         print("Dancing skill")
#         super().skill()
#
# c1=Child1()
# # c1.skill()
#
# c2= Child2()
# c2.skill()
#In python the type of polymorphism it suppport is method overriding
#Its the scenario in which same method is defined (with a different performance) in both parent and child classes

#Method overloading- same method is using more than once in a class.There is no inheritance in this case- does not support in python. only the final method is considered
class Parent:
    def addition(self):
        print("addition of numbers")

    def addition(self,a,b):
        print(a+b)

p1=Parent()
# p1.addition()  - need arguments
p1.addition(10,20)
#






