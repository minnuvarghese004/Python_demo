#Lambda functions- it is a small anonymous function written mostly as a single expression using
# lambda keyword
#Unlike a normal function created using def keyword, a lambda function does not require a function name
#or an explicit return statement
#syntax
#lambda parameters:expression
#expression operation performed and automatically returned as a result

#Write a function for the addition of two numbers
def addition(a,b):
    return a+b
x=addition(2,5)
print(x)

#using lambda function
add=lambda a,b:a+b
print(add(2,5))

#write a lambda function to find a square of the number
# square=lambda a:a*a
# print(square(2))

#check whether a number is even or odd
result=lambda a:"even" if a%2==0 else "odd"
print(result(10))

#non parameterized lambda function
greet=lambda :"Good morning"
print(greet())

#String based questions
#Check whether a given character is a vowel or not (input-x="A")
#Check whether a given character is a consonant or vowel (input-x="A")
#Count the number of vowels in a user input (input x="python")
#Count the number of vowels in a user input (input x="python is easy to learn")
#Loop based questions
#get the count of multiples of 5 from the below list (input x = [1,5,10,15,8,4]
#identify the most repeated element in the given list [5,10,5,10,5,3,2]
#count the number of strings from the below list [5,10,"A","python","hello",3.5,False]


