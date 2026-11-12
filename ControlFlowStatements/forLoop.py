#Write a python program to print "hello world" 10 times
#syntax : for item in iterable
#iterables - string,list,tuple,set,dictionary, range of numbers
# for item in range(10):  #[0,1,2,.....9]
#     print(item," - hello world")
# print("hi")

#Write a python program to iterate first 10 natural numbers (1,2,3...10)
#syntax of range(starting index,ending index+1,step)
# for x in range(1,11):
#     print(x)

# Write a python program to iterate 15 to 35
# for x in range(15,36):
#     print(x)

#Write a python program to iterate first 10 natural numbers and print all even numbers
#method 1
# for i in range(2,11,2):
#     print(i)
#method 2
# for i in range(1,11):
#     if i%2==0:
#         print(i)

##Write a python program to iterate first 10 natural numbers and get even and odd numbers in
#separate list
# even =[]
# odd = []
# for i in range(1,11):
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)

#Write a python program to iterate first 10 natural numbers and get the square of all numbers in separate list
# squares=[]
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)

#Write a python program to iterate first 10 natural numbers (1,2,3...10) and get the sum of squares
# total=0
# for i in range(1,11):
#     #total=total + i**2
#     total+=i**2
# print(total)

#get the sum of first 20 natural numbers
# total =0
# for i in range (1,21):
#     total+=i
# print(total)

#WAP to get the product of first 10 natural numbers
# product =1
# for i in range(1,11):
#     product = product*i
# print(product)

#WAP to get the sum of cubes of first 5 natural numbers
# total=0
# for i in range(1,6):
#     total=total+(i**3)
# print(total)

#WAP to get the sum of cubes of first 10 even numbers
# total=0
# for i in range(2,21,2):
#     #if i%2==0:
#         total = total+(i**3)
# print(total)

#for loop with list
# list1 = [10,20,30,40]
# for i in list1:
#     print(i)

#tuple with list
# tup = (20,30,40,"hello")
# for i in tup:
#     print(i,end=" ") # will print in single line

# s="hello"
# for i in s:
#     print(i)

# s="hello-good mor-ning"
# print(s.split("-"))   # split based on the space

# s="python training"
# for i in s.split():
#     print(i)

#dictionary iteration
# dict1={"name":"Minnu","age":20}
# for key,value in dict1.items():
#     print(key,value)


