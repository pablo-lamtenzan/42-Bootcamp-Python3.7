from matrix import Matrix
from vector import Vector

x = Matrix([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]])
y = Matrix([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]])
z = x + y
print(z.data)
print(z.shape)
z = x - y
print(z.data)
print(z.shape)
z = x * y
print(z.data)
print(z.shape)
z = x / y
print(z.data)
print(z.shape)

v = Vector((3))
z = x * v
print(z.data)
print(z.shape)
