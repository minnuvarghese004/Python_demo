#String based questions
#Check whether a given character is a vowel or not (input-x="A")
# vowels = ["A","E","I","O","U","a","e","i","o","u"]
# character= lambda x:"vowel" if x in vowels else "not a vowel"
# print(character("e"))

#Check whether a given character is a consonant or vowel (input-x="A")
# vowels = ["A","E","I","O","U","a","e","i","o","u"]
# character= lambda x:"consonant" if x not in vowels else "vowel"
# print(character("i"))

#Count the number of vowels in a user input (input x="python")
# vowels = ["A","E","I","O","U","a","e","i","o","u"]
# x = "aeiou"
# count=0
# i=0
# while i<len(x):
#     if x[i] in vowels:
#         count+=1
#     i+=1
# print(count)

#Count the number of vowels in a user input (input x="python is easy to learn")
# vowels = ["A","E","I","O","U","a","e","i","o","u"]
# x ="python is easy to learn"
# count=0
# i=0
# while i<len(x):
#     if x[i] in vowels:
#         count+=1
#     i+=1
# print(count)


#Loop based questions
#get the count of multiples of 5 from the below list (input x = [1,5,10,15,8,4]
# x= [1,5,10,15,20,4]
# count=0
# for i in x:
#     if i%5==0:
#         count+=1
# print (count)

#identify the most repeated element in the given list [5,10,5,10,5,3,2]
x = [5,10,5,10,5,3,2]
for num in x:
    print(x.count(num))

#count the number of strings from the below list [5,10,"A","python","hello",3.5,False]