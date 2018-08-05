# Example

t = (1, 2, 3, 4, 5)

print(len(t))
print(1 in t) # 1 2 3 4 5 - iterate
t[0] = 10 #'tuple' object does not support item assignment

t2 = t + (200, 300)

print(t2)
print(t*2)
print(t2[0], t2[-1])

#t[start: end: step]
print(t[::-1]) # reverse
print(t[::2]) # odd places
print(t[1 : 5 : 2]) # even places

print(type( (1))) # integer
print(type( (1,))) # tupple

# Converting data types
t = (1, 2, 3, 4, 5)
l = list(t * 2)
print(l)

## Reference structure
l = [1, 2, 3]
ll = [l, l, l]
ll[-1][-1] = 30
print(ll)
print(l)

# Without Reference : Immutabless
ll = [l.copy(), l[:], l[:]]
ll[-1][-1] = 30
print(ll)
print(l)

#Infinite reference
l += [l]
print(l)
print(l[-1])