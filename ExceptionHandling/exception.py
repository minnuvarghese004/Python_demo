#Error- A problem in a program that prevents it from working as intended
#Reasons
#1.Incorrect syntax
#2.Incorrect program logic
#3.Invalid operations

#Eg:
# if 10>5
#     print("hello")
#Eg for syntax error

#print(name)  - NameError

# list1=[10,20,30]
# print(list1[5])  -IndexError

# number=int("hello") -ValueError

# print(10/0)  -ZeroDivisionError

# dict1={"name":"minnu","age":25}
# print(dict1["location"])   -KeyError

# Exception - it's an error that occurs during program execution and interrupts the normal flow of the program
#Syntax
# try:
#     # code that may cause an exception
# except:
#     # code to handle the exception
# else:
  # executes when no exception occurs
# finally:
  # executes irrespective of exception

# try:
#     num=int(input("Enter a number: "))
#     result=100/num
#     print(result)
# except ValueError:
#     print("Please enter a valid integer")
# except ZeroDivisionError:
#     print("Please enter a non zero value")
# print("hello")

# try:
#     num=int(input("Enter a number: "))
#     result=100/num
#
# except ValueError:
#     print("Please enter a valid integer")
# except ZeroDivisionError:
#     print("Please enter a non zero value")
# else:
#     print(result)
#     print("No exception occured")
# finally:
#     print("program execution completed")

#raising exceptions using raise keyword- if want to generate an intentional exception when a particular condition occurs
#Eg:
# age=17
# if age<18:
#     raise ValueError("Age must be 18 above")
# print("Eligible")

def withdraw(balance,amount):
    if amount>balance:
        raise ValueError("Insufficient balance")
    else:
        return balance-amount

x=withdraw(100,50)
print(x)
y=withdraw(50,200)
print(y)

#Exception handling in playwright
#1.Element not found
#2.Locator too long to become actionable
#3.Browser gets closed unexpectedly

