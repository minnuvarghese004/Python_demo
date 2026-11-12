# print("hello")
x = 10
# print(x)
# variable x is declared and value 10 is assigned/initialized
x=20
print(x)
# Declaration alone cannot be performed and while reinitializing first value get removed
print(type(x)) # type checking using type method

#  basic datatypes in python - integer, boolean, float,string ( basic datatype can store only one value at a time)
y = 20
print(type(y))
y = 20.5
print(type(y))
y = True
print(type(y))
y = "ABC  123@#$$"
print(type(y))
"""
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'str'>
"""
# Collection datatypes / data structures - can store multiple values in a single variable
# List, Tuple, set, dictionary

x= list()  # only declaration , no value assigning
x = [10, 10.5, True, "hello", 10,10]     #declaration and value assigning
print(x)
# List features - ordered, duplication allowed, mutable, indexing, slicing

print(x[0])
print(x[2])




