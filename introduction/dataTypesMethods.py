#Mutable data types - list,set,Dictionary
#Immutable data types-Integer, Float,String,Boolean,Tuple

#keywords - They are reserved meaningful words in Python, cannot be provided as a variable name
"""import keyword
print(keyword.kwlist)
#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

#Difference between keyword,identifier and variable:
#variable  declaration can be performed to store or assign values
#Variable declaration examples
x=10
X=20
abcAB=30
abc_=40
_abc=50
abc_def=60
_=50
abc123=70
a12_c=80
#12abc=90 cannot start with a digit, spaces are not allowed
#Must starts with a letter or underscore, special characters are also not allowed

#Idetifiers are variable which are meaningful in nature
name = "Minnu"
age = 36
price = 1.5

#case sensitivity in python
#Unicode represents a character's individual code of representation in normal english
x=10
X= 20
print(X)

a="Python"
b="python"
print(a==b) #check both case and value and return a boolean response

#String Methods
str1 = "Minnu ABC is a student"
print(str1.upper())
x= str1.lower()
print(x)
print(str1.capitalize())  #First letter of first word get uppercase
print(str1.title()) # First letter of all words get uppercase
print(str1.swapcase()) #swap the cases
print(str1.find("is")) #returns the first position of a substring
print(str1.index("is")) #returns the first position of a substring
print(str1.count("a"))
print(str1.isupper())
print(str1.isdigit())
print(f"The original string is :{str1}")
"""

#List methods
"""list1 = [1,2.5,"Minnu"]
list1.append("Varghese")
print(list1)
list1.pop()
print(list1)

list2=[3,4,"Apple"]
list1.extend(list2)
print(list1)

list1.insert(0,"Orange")
print(list1)

list1.append(2.5)
#list1.remove(2.5) #removes only the first occurence of the elements
print(list1)
print(list1.count(2.5))
#list1.clear()
print(list1)
#list1.reverse()
print(list1)
list3=list1.copy()
print(list3)
list4=[10,2.5,0,-10,100,0.5]
list4.sort() #to convert in ascending order
print(list4)
list4.sort(reverse=True) #to convert in descending order
print(list4)
list5 = ["book","pen","Z","K","d","BOOK","PEN","Apple","aPPLE"]
list5.sort()#Convert in alphabetical order. First preference for Uppercase
print(list5)
#Methods - append,pop,insert,extend,clear,copy,sort,reverse,remove

#Built-In methods in Python list
num = [2,1,10,100,2.5]
print(len(num))
print(max(num))
print(min(num))
print(sum(num))"""

#Interview question
# list6=[10,20,30,40]
# name="ABC"
# #Expected output [10,20,"ABC",30,40]
# list6.insert(2,"ABC")
# print(list6)
#---------

#Tuple methods
num =(2,3,3,10,5.5,100.5)
print(num.count(3))
print(num.index(5.5))
#Create a tuple and add a new element in its second last index position
num=list(num)
num.insert(-2,"Grapes")
print(num)
num=tuple(num)
print(num)

#packing and unpacking of tuple
student =("Minnu",36,"female","Ernakulam","Kollam")
name,age,gender,*place = student
print(age,gender,name)
print(place)

tuple1= ("a","b","c","D","E")
x,*y,z = tuple1
print(x,z)
print(y)

#Dictionary Methods
dict1 ={"Name":"Minnu","Age":20,"Gender":"female"}
print(dict1["Name"])
print(dict1.get("Age"))
dict1["Location"]="Kollam"
print(dict1)
dict1.update({"Age":30})
print(dict1)
dict1["Name"]= "Aswathy"
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())
#Each key value pair in a dictionary is called as an Item
#print(dict1[0]) - index cannot be used in dict





