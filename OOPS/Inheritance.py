#4 pillars of OOPS
#Inheritance: It is the concept in which one class acquires the properties and methods of another class
#The first class is called as - parent,base,super
#The second class is called as - child,subclass, derived class,inherited class
#A child class can reuse the code of a parent class without writing it again

class Parent:
    networth="10 crore"

    def skill(self):
        print("Teaching skill")

class Child(Parent):
    def job(self,jobTitle):
        print(f"Job title is {jobTitle}")


c=Child()
c.skill()
print(c.networth)
c.job("HR")

#Types of inheritance
#1.Single inheritance - one parent one child
#2.Multiple inheritance- diff parent class and single child class
#3.Multilevel Inheritance - A child class becomes parent class for another class
#4.Hierarchial inheritance - single parent and diff child
#5.Hybrid inheritance - can be combination of 2 or more types of inheritance

#Multiple inheritance
class A:
    pass
class B:
    pass
class C(A,B):
    pass
c=C()

#Multilevel Inheritance
class A:
    pass
class B(A):
    pass
class C(B):
    pass
c=C()

#Hierarchial Inheritance
class Parent:
    def display(self):
        print("Parent method")
class Child1(Parent):
    pass
class Child2(Parent):
    pass

c1=Child1()
c1.display()
c2=Child2()
c2.display()


