
for i in range(1, 6):
    line = ""
    for j in range(1, 6-i):
        line += " "


    for k in range(0, 2*i-1):
         line += "*"
    print(line)