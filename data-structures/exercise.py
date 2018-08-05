D1 = {'ok' : 1, 'nok': 2}
D2 = {'ok': 2, 'new': 3}

# Create Below

# 1. Union of keys, # values does not matter
#    D_Union = {'ok': 1, 'nok': 2, 'new': 3}

# solution:
D3 = D1.copy()
for d in D2:
    D3[d] = D2[d]
print(D3)

# 2. Intersection of keys; # values doesnot matter
#    D_Intersection = {'ok': 1}

#solution:
D3 = {}
for d in D1:
    if d in D2:
        D3[d] = D1[d]
print(D3)

# 3. Difference
# D1 - D2 = {'nok': 2}

# solution:
D3 = {}
for d in D1:
    if d not in D2:
        D3[d] = D1[d]
print(D3)

# 4. Sum
# # values are aded for same keys
# D_merge = {'ok': 3, 'nok': 2, 'new': 3}

# solution:
D3 = D1.copy()
for d in D2:
    if d in D3:
        D3[d] += D2[d]
    else:
        D3[d] = D2[d]
print(D3)