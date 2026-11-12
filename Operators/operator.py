#Arithmetic Operators - +,-,*,%,/,//,**
"""a,b=10,20  #can include diff data type
print(a+b)  #30
print(a-b)  #-10
print(a*b)  #200
print(a/b)  #0.5 (normal divsion)
print(a//b) #0 -removes decimal part -floor division
print(a%b)  #reminder (modular division)
print(a**2) #base**exponent = 10^2

a,b="hello","Minnu"
print(a+b)#concatination
a,b = 10+"hello"
print(a+b)"""

#comparison operators - >,<,<=,>=,=,==,!= (returns a boolean value)
a,b=20,"20"
#print(a>b)
print(a==b)  #checks both value and data type are equal or not
print(a!=b)

#Assignment operators
a,b=10,20
a=a+b
print(a)  #30

a,b=10,20
a+=b #possible for all arithmetic operators
print(a) #30

#Logical operators -and,or,not - returns boolean value
a,b,c=10,20,30
print(a<b and b<c and c>a) # returns true if all conditions are true
print(a<b or b<c or c>a) #if any one of the condition is true, returns true
print(not b>c) #to handle the reverse case

#Membership operators - in,not in
a="hello"
print("O" in a)
b=[10,20,30,40]
print(50 not in b)

#identity operators - is,is not (equal as == ,!=)
a,b=10,20
print(a is b)


