#Print numbers from 1 to 5
# i=1
# while (i<=5):
#     print(i)
#     i+=1

#Sum of the first 5 natural numbers
# total=0
# i=1
# while(i<=5):
#     total+=i
#     i+=1
# print(total)

#Product of the first 5 natural numbers
# prod = 1
# i=1
# while(i<=5):
#     prod*=i
#     i+=1
# print(prod)

#Print even numbers from 2 to 10
# i=2
# while(i<=10):
#     print(i)
#     i+=2

#Print numbers in reverse order
# i=5
# while(i>=1):
#     print(i)
#     i-=1

#Ask the user to enter a number until they enter 0
# num= int(input("enter 0 to stop: "))
# while(num!=0):
#     print(f"you enetered: {num}")
#     num = int(input("enter 0 to stop: "))
# print("Stopped")

#Multiplication Table
# num= int(input("Enter a number"))
# i=1
# while (i<=10):
#     mult= i*num
#     print(f"{i} * {num}= {mult}")
#     i+=1

#sum of digits
# num=int(input("enter a number: "))
# total =0
# while(num>0):
#     total=total + num%10
#     num =num//10
# print(total)

#Reverse a Number
# num = int(input("enter a number: "))
# reverse =0
# while(num>0):
#     digit= num%10
#     reverse = reverse*10 + digit
#     num= num//10
# print(reverse)

#Or
num = input("enter a number: ")
reverse=""
i=len(num)-1
while(i>=0):
    reverse = reverse+num[i]
    i-=1
print(reverse)




