#if,elif,else
#input an age from user and check whether he is minor or not

"""age = int(input("Enter your age: "))
if age >=18:
    print ("you are an adult")
else:
    print("You are minor")"""

#input an age and nationality from user and check whether he is eligible for voting or not
"""age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ").lower()
print(nationality)
if (age>=18 and nationality=="indian"):
    print ("Your are eligible")
else:
    print("You are not eligible")"""

#input a number from user and check if it is even or odd
"""a = int(input("Enter your age: "))
if a%2==0:
    print("Your age is even")
else:
    print("Your age is odd")"""

#input a number and check whether it is divisible by 5 or not
"""num1= int(input("Enter a number: "))
if num1%5==0:
    print("Number is divisble by 5")
else:
    print("Number is not divisible by 5")"""

# check a number is positive or not
"""num2 = int(input("Enter a number: "))
if(num2>0):
    print("Number is positive")
else:
    print("Number is Negative")"""

#check a number is 0 or not
"""num3 = int(input("Enter a number: "))
if(num3==0):
    print("Number is Zero")
else:
    print("Number is not zero")"""

#input the mark , set the passmark and check whether pass or fail
"""mark = int(input("Enter your mark: "))
passMark = 75
if mark >= passMark:
    print("Passed")
else:
    print("Failed")"""

#Enter age ,set entry fee and check eligibility for discount for senior citizen
"""age = int(input("Enter your age: "))
fee = 100
disc_fee = fee - (fee * 10 / 100)
if age>=60:
    print(f"Your age is {age} and ticket fee is {disc_fee}")
else:
    print(f"Your age is {age} and ticket fee is {fee}")"""

#input a number and check it is positive , negative or zero
"""num1 = int(input("Enter a number: "))
if num1>0:
    print(f"{num1} is positive")
elif num1==0:
    print(f"{num1} is Zero")
else:
    print(f"{num1} is Negative")"""

#Input 3 numbers and check which one is greater
"""num1,num2,num3 = 100,20,30
if (num1>num2 and num1>num3):
    print(f"{num1} is greater")
elif (num2>num1 and num2>num3):
    print(f"{num2} is greater")
else:
    print(f"{num3} is greater")"""

#Input mark from user
""">=90 ,Grade A
>=80, Grade B
>=70, Grade C
>=60, Grade D
<60, Fail
<0 or >100, Invalid mark
"""
mark = int(input("Enter the mark: "))
if mark<0 or mark>100:
    print("Invalid mark")
elif mark>=90:
    print("Grade A")
elif mark>=80:
    print ("Grade B")
elif mark >= 70:
    print("Grade C")
elif mark>=60:
    print ("Grade D")
elif mark<60:
    print ("Failed")