from vector import Vector

try:
    print("---------Vector with an int----------")
    v1 = Vector(3)
    print(v1)
    print(v1.T())
    print(v1.shape)
    print("---------Vector with a range----------")
    v1 = Vector((10, 15))
    print(v1)
    print(v1.T())
    print(v1.shape)
    print("---------Vector with a list of floats----------")
    v1 = Vector([0.0, 1.0, 2.0, 3.0])
    print(v1)
    print(v1.T())
    print(v1.shape)
    print("---------Vector with a list of lists of floats----------")
    v2 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print(v2)
    print(v2.T())
    print(v2.shape)
    print("---------ADD---------")
    print(v1)
    print(v1 + v1)
    print(v2)
    print(v2 + v2)
    # print(v1 + v2)
    print("---------SUB---------")
    print(v1)
    print(v1 - v1)
    print(v2)
    print(v2 - v2)
    # print(v1 - v2)
    print("---------DIV---------")
    print(v1)
    print(v1 / 2.0)
    print(v2)
    print(v2 / 2.0)
    # print(2.0 / v2)
    print("---------MUL---------")
    print(v1)
    print(v1 * 2)
    print(v2)
    print(2 * v2)
    print(v1.dot(v1))
    # print(v1.dot(v2))

except ValueError as err:
    print(err.args)

print("++++++++++TEST CORRECTION+++++++++++")
print(Vector([1., 2e-3, 3.14, 5.]).values)
print(Vector(4).values)
# Vector(-1)
print(Vector((10, 12)).values)
# print(Vector((3, 1)).values)
v = Vector((1, 1))
print(v.values)
# Vector((4, 7.1))
v = Vector(4)
print(v.values)
print(v * 4)
print(4.0 * v)
# v * "hi"
v = Vector(4)
v2 = Vector([[1.0], [1.0], [1.0], [1.0]])
print((v + v2).values)
# v + Vector([0.0, 0.0, 0.0, 0.0])
# v + "hello"
# v + None
print((v - v2).values != (v2 - v).values)
print(Vector(4) / 2)
print(Vector(4) / 3.14)
# print(Vector(4) / 0)
# print(Vector(4) / None)
# print(3 / Vector(3))
