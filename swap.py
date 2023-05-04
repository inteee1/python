def swap(a, b):
    tmp = a
    a = b
    b =tmp

def swap2():
    global a, b
    tmp = a
    a = b
    b = tmp



a = 100
b = 200
print("a", a, "b", b)

swap(a, b)

print("a", a, "b", b)

swap2()

print("a", a, "b", b)