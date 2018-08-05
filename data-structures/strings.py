s = 'Hello World'
# output: H 1
#         e 1 
#         l 3 
#         o 2 
#           1
#         W 1
#         r 1
#         d 1

# method: 1
for a in s:
    n = 0
    for b in s:
        if( a == b):
            n = n + 1
    print(a + ' '+ str(n))

# method: 2
d = {}
for b in s:
    if b in d:
        d[b] += 1
    else:
        d[b] = 1
print(d)
for a in d:
    print(a, d[a])

#---------------------------------------#
# substring
print(s[0: 6: 2])
print(s[-len(s)] == s[0])
print(s[::2])
print(s[3:8])

# string methods
print(s.split())
print(len(s.split()))
print(s.startswith("H"))
print(s.startswith("h"))
print(s.endswith("H"))
print(s.strip())
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.title())
