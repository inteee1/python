
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

value = int(input("value : "))

for i in range(0, 10):
    if value == list[i]:
        break

if i == 10:
     print("not found")
else:
     print("found")
if value in list:
    print("found")
else:
    print("not found")

if value not in list:
    print("not found")
else:
     print("found")