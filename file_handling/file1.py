'''my_file=open('file_handling/notes.txt','r')
print(my_file)'''''

my_file2=open('6789.txt','a+')

my_file2.write("\ni i i i i i i i i")
my_file2.seek(0)
print(my_file2.read())
my_file2.close()   