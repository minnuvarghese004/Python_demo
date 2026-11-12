#In file handling ,for testing purpose the most commonly used files are txt,json and excel.
#txt file
#Using built-in open() function
#Opening file in read mode
# file=open("data.txt","r")
# content=file.read()
# print(content)

file1=open("data.txt","r")
content=file1.readlines()
print(content)

file1=open("data.txt","r")
content=file1.readline()
print(content)

#opening files in write mode
#new_file = open("data.txt","w")
#new_file.write("hello")    #existing data will be replaced

new_file = open("data1.txt","w")
new_file.write("name:Akhil")

#opening files in append mode
file =open("data.txt","a")
file.write("contact:12345 \n")
file.close()
print(file.closed)

#methods applicable in existing file - read, write,append,create
#methods applicable in non existing file - write(w),append(a),create(x)

#File handling using with statement
#With statement automatically closes the file when the block finishes even if an exception occurs
with open("data.txt","r") as file2:
    content=file2.read()
    print(content)
    print(file2.closed)

print(file2.closed)






