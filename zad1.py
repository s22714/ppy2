import sys

a = b = c = "Python 2023"
#print(sys.getrefcount(a))

print(a == b)
print(b == c)

print(type(a))
print(type(b))
print(type(c))

print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))

c = "Java 11"

print(a == b)
print(b == c)

print(type(a))
print(type(b))
print(type(c))

print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))