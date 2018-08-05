# Set : {}
# ----------
# - Indexing, Duplicate, Insertion Order not allowed
# - Frozenset - Immutable set

#Examples: Set

s = {1, 2, 3, 4, 5, 1, 2, 3}
print(s)
print(len(s))
print(3 in s)

print({1, 2} == {2, 1})  # True
print([1, 2] == [2, 1])  # False

#Set Operations

## Union - |
a = s | { 5, 6 }
print(a)

## Intersection - &
b = s & {5, 6}
print(b)

## Difference : -
c = s - {5, 6}
print(c)

## Exor - ^
d = s ^ {5, 6}
print(d)

s.append(40) # Error


# Bytes

b = b'Hello'
sr = "Hello"

print(sr.encode("utf-8"))
print(sr.encode("utf-8").decode("utf-8"))

s1 = set(dir(bytes))
s2 = set(dir(str))

print(len(s1 - s2))


# List of sets

ls = [{1, 2}, {3, 4}]
sl = {[1, 2], [3, 4]}
print(sl) # TypeError: unhashable type: 'list' 


# Hash
hash(1)  # 1
print( hash( (1,2) ) )
print( hash( (2,1) ) )


print(hash( [1, 2] )) # TypeError: unhashable type: 'list'
s = { (1, 2), (3, 4) }
print( s )

print(s is s)
print( s is not {1, 2})