## Dictionary ( key and value)
# ----------------------------
# - O notation
# - Key is unique
# - Order doesn't matter

d = {'nok' : 1, "ok": 2}
print(d['ok'])
d['nok'] = 3
print(d['nok'])

for key in d:
    print(key, d[key])

for k, v in d.items():
    print(k, v)

# Nested dict
d = {"ok": 2, "nok": 3}
c = 0
while c < 3:
    d = {"ok" : [d]}
    c += 1
print(d)
d['ok'][0]['ok'][0]['ok'][0]['nok'] = 30
print(d)