str = input("a, b, c: ")
list = str.split()
a = int(list[0])
b = int(list[1])
c = int(list[2])

if a > b:
    max = a
    min = b
else:
    max = b
    min = a
if c > max:
    mid = max
    max = c
elif c > min:
    mid = c
else:
    mid = min
    min = c

print(f"max : {max} mid : {mid} min : {min}")