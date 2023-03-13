a = 4000
b = 4000
print(id(a))
print(id(b))

a = b = 4000
print(id(a))
print(id(b))

b = 3000
print(id(a))
print(id(b))
print(a)

a = 30.6
b = "Tekst"
c = True
print(type(a))
print(type(b))
print(type(c))

print(bool(1))
print(bool(0))
print(bool(-1))

print(bool("Text"))
print(bool(""))

