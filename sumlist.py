
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
for i in range(0, 10):
    total += list[i]

print("total : ", total)

total = sum(list)
print("total : ", total)
average = sum(list) / len(list)
print("average : ",average)