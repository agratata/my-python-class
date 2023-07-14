#len str string.upper, string.lower string.split split join replace
s1="Samriddha"
s2="rhododendron"
s3=45

print(len(s1),len(s2))
print(type(str(s3)))
print(s1.upper())
print(s1.lower())

s2=s2.split("d")
print(s2)
#output ['rho', 'o', 'en', 'ron']

#string.join(list)
print("d".join(s2))

#string.replace(oldvalue, newvalue, count)
s4="i like shiny things"
print(s4.replace("shiny","bright"))