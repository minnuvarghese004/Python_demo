#Constructor is a special method that get automatically called or invoked when an object is created
#purpose- Initialize object atrributes,assign initial values to variable,perform initial setup

class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Constructor created")

    def display(self):
        print("Parent method")
        print(self.name,self.age)

obj=Parent("Minnu",20)
obj.display()

obj2=Parent("Chinnu",30)
obj2.display()

#Destructor
#A destructor also a special method python may call when an object is about to be destroyed
#purpose- perform cleanup operations,close files or connections

class Parent:
    x=10
    def __init__(self):
        print("Constructor created")

    def __del__(self):
        print("Destructor created")

parent1=Parent()
del parent1
print(parent1.x)

