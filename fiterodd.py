
list = [ i for i in range(1, 11)]
print("list: ",list)
i = 0
while i < len(list):
    if list[i] % 2 != 1:
        #list.remove(list[i]) #값을 찾아서 확인
        #del list[i]
        list.pop(i)
    i += 1

print("list: ", list)