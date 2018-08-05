# List : []
# ------------------
# - Indexing Possible
# - Duplicates allowed
# - Insertion Order
# - Mutable

# Examples: 

l = [1, 2, 3, 4.0, "ok", [1,2]]

print(len(l))
print("nok" in l)
print(l == [1,2])

# interate
for a in l:
    print(a)

l[0] = 200
print(l)

# immutable append
l2 = l + [300]
print(l, l2)

l += [301]
print(l, l2)

# in place append
l.append("nok")
print(l, l2)
l2.insert(4,5)
print(l, l2)

l = [1, 2, 3, 4, 5]

# insert at start
l[:0] = [99, 100]
print(l)

# insert at end
l[len(l):] = [99, 100]
print(l)

# insert at 2 and before 2
l[2:2] = [99, 100]
print(l)

l[2:5] = [200]
print(l)

l[::2] = ["ok"] * len(l[::2])
print(l)


# Range
l1 = list(range(0, 5, 1))
print(l1)
l = []
c = 0
while c < 3:
    l = [l]
    c += 1
print(l)

#nested list
l = [[[[1, 2, 3, 4, 5]]]]
l[0][0][0][4] = 500
print(l)