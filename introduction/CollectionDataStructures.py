# Collection datatypes / data structures - can store multiple values in a single variable
# List, Tuple, set, dictionary

x= list()  # only declaration , no value assigning
x = [10, 10.5, True, "hello", 10,10]     #declaration and value assigning
print(x)
# List features - ordered, duplication allowed, mutable, indexing, slicing

print(x[0])
print(x[2])

#slicing
# collect the elements at indexes 0,1,2
print(x[0:3])
y = x[2:6]
print(y)

length_x = len(x)
print(length_x)

print(x[0:])
print(x[:6])
print(x[:])
print(x[0:6:2])
#slicing syntax [starting index : ending index +1 :step]

# negative indexing
x = [10, 10.5, True, "hello", 10,10]
print(x[-3])
print(x[-5:-2]) # collect the elements in indexes -5,-4,-3

#Tuple - it is the immutable collection data structure in python
x= tuple()
print(x)
print(type(x))
x=(3,4.5, False, "Minnu", 10,10, [2,4,6], (100,200))
print(x)
#Tuple Features ; Ordered, Duplications allowed, indexing, slicing, multi data storage
# Tuple is faster than list in case of large number of data - as it is immutable

#Set
x=set()
print(x)
print(type(x))
x={2}    # empty {} denote dictionary, atleast 1 value required to make it as a set
print(type(x))
x={2,2.5,True,"Minnu",10,10}
print(x)

#set features - Unordered, no duplication, no indexing, no slicing, mutable, cannot add list or tuples

#Dictionary - The only named index data structure in python
x= dict()
x= {"name":"Minnu","Age":36, "Gender":"female","name":"ABC", "Contact": [123,456,789]}
print(x)
print(x["name"])
print(x["Contact"])
print(x["Contact"][1])























