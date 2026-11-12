#Write a python program to check whether a number is prime or not
# num = int(input("Enter a number: "))
#
# if num<=1:
#     print("Not a prime number")
# else:
#     for i in (2,num-1):
#         if num%i==0:
#             print("Not a prime")
#             break
#     else:
#         print("Prime")
#
#Find the prime numbers in a range 10 to 30
# prime=[]
# for num in range (10,31):
#     if num<2:
#         print("Not a prime")
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             prime.append(num)
# print(prime)

#Find the count of prime numbers in a range 10 to 30
# prime=[]
# prime_count=0
# for num in range (10,31):
#     if num<2:
#         print("Not a prime")
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             prime.append(num)
#             # prime_count+=1
# print(prime)
# print(len(prime))

#Input a number from user and reverse it (input=541 output =145)
# num=int(input("Enter a number: "))
# reverse=0
# while num>0:
#     digit=num%10
#     reverse = reverse*10 + digit
#     num=num//10
# print(reverse)

# string reverse
# text = "python"
# print(text[::-1])
# str1="hello"
# rev=""
# for i in str1:
#     rev= i + rev
# print(rev)
# str1= "e"+"h"
# print(str1)

#Input a  number from user and find the sum of digits of number
#input 541 output 5+4+1 =10
# num=int(input("Enter a number: "))
# org=num
# digit_sum =0
# while num>0:
#     digit_sum+=num%10
#     num=num//10
# print(f"Sum of digits of {org} is {digit_sum}")

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
x= [100,10,-1,1200,11,3]
largest=x[0]
for i in x:
    if i>largest:
        largest=i
print(largest)


















