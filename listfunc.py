my_list=[10,20,30,40]
my_list.append(100)
print(my_list)

print(len(my_list))
print(max(my_list))
print(min(my_list))
print(sum(my_list))

#tuple, my_list anything is valid
m5=(5,10,15,20)
my_list.extend(m5)

#my_list.insert(index,element)
my_list.insert(0,1)
print(my_list)

print(sorted(my_list))