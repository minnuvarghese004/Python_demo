#WAP to iterate first 10 natural numbers
# for i in range(1,11):
#     print(i)

# i=1
# while (i<=10):   #while true - loop continues
#     print(i)
#     i+=1

#iterate numbers 20 to 40
# i=20
# while (i<=40):
#     print(i)
#     i+=1

# iterate first 10 natural numbers in reverse order
# i=10
# while (i>0):
#     print(i)
#     i-=1

#for loop is generally used when we want to iterate over a sequence (list, tuple) or to repeat a known number of time
#eg: iterate 1 to 5, iterate 1 to 10
# while loop is used when we want to repeat a block of code as long as the condition is True
#eg: to login with valid credentials, ATM cash withdrawal using pin

#WAP to find the factorial of a number
#eg: for number 5, factorial = 1*2*3*4*5=120
# num1=int(input("Enter a number: "))
# factorial=1
# for i in range(1,num1+1):
# # for i in (1,num1):
#     factorial*=i
# print(f"The factorial of {num1} is {factorial}")

#WAP that repeatedly ask the user to enter a username and password until both credentials are correct
# usrname= "admin"
# pwd = "admin123"
#
# user1 = ""
# pwd1 = ""
# while (user1 !=usrname or pwd1 != pwd):
#     user1 = input("Enter username: ")
#     pwd1 = input("Enter password: ")
#     if (user1!=usrname or pwd1 !=pwd):
#         print("Invalid credentials Try again")
# print("Login successfull")

#ATM pin verification- provide a valid pin number, get a pin from user and check the validity
valid_pin = "1234"
pin = ""
while pin != valid_pin:
    pin = input("Enter your ATM PIN: ")
    if pin != valid_pin:
        print("Invalid PIN. Try again")
print("PIN verification successful")
