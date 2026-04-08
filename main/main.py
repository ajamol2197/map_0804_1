# 1
a = [1, 1, 6, 4, 3]
print(a)

y = list(map(lambda b: b * b, a))
print(y)

# 2
a = ['ali', 'vali']
print(a)

v = list(map(lambda o: o.upper(), a))
print(v)

# 3
a = [1, 1, 6, 4, 3]
print(a)

y = list(map(lambda b: b * 2, a))
print(y)

# 4
a = ['ali', 'vali']
print(a)

v = list(map(lambda o: len(o), a))
print(v)

# 5
c = [3]
print(c)

v = list(map(lambda f: f + f, c))
print(v)

# 6
d = [3, 8, 9, 6, 5]
print(d)

a = list(map(lambda f: abs(f), d))
print(a)

# 7
a = ['ali', 'vali']
print(a)

v = list(map(lambda o: o[::-1], a))
print(v)

# 8
a = [3, 9, 7, 6, 6]
print(a)

v = list(map(lambda o: o * o * o, a))
print(v)

# 9
a = ['ali', 'vali']
print(a)

v = list(map(lambda o: o[0], a))
print(v)

# 10
a = [3, 9, 7, 6, 6]
print(a)

v = list(map(lambda o: "Juft" if o % 2 == 0 else "Toq", a))
print(v)

# 11
a = [2]
print(a)

b = list(map(lambda g: g * g, a))
print(b)
