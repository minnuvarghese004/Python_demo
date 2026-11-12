#Encapsulation
#It is the process of combining data(variables) and methods(functions) into a single unit(class) called a class and while controlling access to the data
#Python has 3 common access levels(Access modifiers)
#1.public- (name="Minnu") can be accessed normally
#2.protected (_name="Minnu") intended for internal or subclass uses
#3.private (__name="Minnu") can be accessed only using base class objects
#Example for private variable-password
#Eg for private method- balance enquiry using atm card

class Employee:
    def __init__(self,name,salary,password):
        self.name=name   #public variable
        self._salary=salary  #protected variable
        self.__password=password  #private variable

    def display_name(self):                       #public method
        print(f"Employee name is {self.name}")

    def _display_salary(self):                    # protected method
        print(f"Emplyee salary is {self._salary}")

    def __display_password(self):                  #private method
        print(f"Employee Password is {self.__password}")

    def show_details(self):
        self.__display_password()

obj=Employee("Minnu",40000,"ABC123")

#Accessing public variable and method
print(obj.name)
obj.display_name()

#Accessing protected variable and method
print(obj._salary)
obj._display_salary()

#Accessing private variable and method
#print(obj.__password)         #error - no attribute
# obj.__display_password       #cannot access private variable and method directly
obj.show_details()

#getter and setter methods
#getter method - it's a method used to retrieve the value of a private variable
#setter method - used to modify the value of a private variable usually with validation

