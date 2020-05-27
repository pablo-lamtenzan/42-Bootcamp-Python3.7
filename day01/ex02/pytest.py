from vector import Vector

x = Vector([0.5, 42.0, 10.0])
# different dimensions are ignored
y = Vector([0.5, 100.0, 0, 2])
f = Vector(3)
print(f.values)
w = Vector((12, 15))
print(w.values)

print("ADDITION TEST")
z = x + y
print(z.values)
print(z.size)
z = x + "some error type"
print(z.values)
print(z.size)

print("SUBS TEST")
z = x - y
print(z.values)
print(z.size)
z = x - "some error type"
print(z.values)
print(z.size)

print("DIVITION TEST")
z = x / y
print(z.values)
print(z.size)
z = x / "some error type"
print(z.values)
print(z.size)

print("PRODUCT TEST")
z = x * y
print(z.values)
print(z.size)
z = x * "some error type"
print(z.values)
print(z.size)

print("STR TEST")
print(z.__str__())

print("REPR TEST")
print(z.__repr__())

print("TRASH ARG TEST OBJ")
z = Vector("trash")
print(z.values)
print(z.size)
z = Vector()
print(z.values)
print(z.size)