# !/usr/bin/python3

class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return "Vector({}, {})".format(self.a, self.b)

   def __add__(self, other):
      return Vector(self.a + other.a, self.b + other.b)

   def __sub__(self, other):
      return Vector(self.a - other.a, self.b - other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
v3 = Vector(4,2)
result = v1 + v2 - v3
print(result)