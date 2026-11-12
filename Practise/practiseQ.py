#Write a python program to check whether a number is prime or not
#prime numbers - 2,3,5,7,11,13,17 (Those numbers which are divisible by 1 and same number only)
#Eg: consider 7 (Divide using 2,3,5,6).If remainder is 0 in any case , number is not prime
#Consider 9 (Divide 2 to 8)
# num = int (input("Enter a number: "))
# if num<2:
#     print("Its not in prime number range")
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print(f"{num} is not prime")
#             break
#     else:
#         print(f"{num} is prime")

#Find the prime numbers in a range from 10 to 30
# prime=[]
# for num in range(10,31):
#     if num<2:
#         print("Its not in prime number range")
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             prime.append(num)
# print(prime)

#Find the count of prime numbers in a range from 10 to 30
# prime=[]
# count=0
# for num in range(10,31):
#     if num<2:
#         print("Its not in prime number range")
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             prime.append(num)
#             count+=1
# print(prime)
# print(len(prime))
# print(count)

#input a number from user and reverse it (input: 541,output :145)
num = 541
reverse=0
while num>0:
    digit = num%10
    reverse = reverse*10 + digit
    num//=10
print(reverse)
#In first iteration, n=541, digit = 1, reverse = 0*10 +1 =1, n=54
#In second iteration, n= 54, digit= 4, reverse = 1*10 + 4= 14,n= 5
#In third iteration, n= 5, digit = 5, reverse = 14*10 +5= 145,n=0
#In 4th iteration, condition False and while loop breaks

#input a number form user and find the sum of digits of the number
#Input = 541 and output =10
# num = int (input ("Enter a number: "))
# org=num
# sum =0
# while num >0:
#     sum = sum + num%10
#     num//=10
# print(f"sum of digits of num is {org} is {sum}")

#input a string from user and remove all duplicate characters
#input = programming, output= progamin
# str1= input("Enter a string: ")
# result=""
# for i in str1:
#     if i not in result:
#         result=result+i
# print(result)

#Input 2 numbers from user and swap it
#input=a,b=10,20
#output=a,b=20,10

# a=int(input('enter first number: '))
# b=int(input('enter second number:'))
#
# c=a
# a=b
# b=c
# print(f"Swapped result a={a} and b={b}")

# Find the largest number in a list without using index position
#x=[100,10,-1,1200,11,3]
#output = 1200

# x= [100,10,-1,1200,11,3]
# print(max(x))
# x= [100,10,-1,1200,11,3]
# largest=x[0]
# for i in x:
#     if i>largest:
#         largest=i
# print(largest)
