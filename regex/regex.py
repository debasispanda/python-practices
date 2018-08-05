import re

s = "Hello World Ok"
print(dir(re))
print(re.findall(r"\w+", s))
print(re.split(r"\s+", s))

x = "Name:xyz,age=40"
print(re.findall(r"Name:(\w+)", x))
print(re.sub("Name:(\w+)", r"Name:\1", x))

# x = "Name:xyz,age=40|Name:abc,agc=50"
# output = "Name:Xyz,age=40|Name:Abc,age=50"

#solution
l = re.split(r"\|", x)
t = ""
k = []
for n in l:
    bb = re.findall(r"Name:(\w+)", n)
    f = bb[0].capitalize()
    g = re.sub(r"Name:(\w+)", "Name:"+ f, n)
    k.append(g)
t = "|".join(k)

print(t)

