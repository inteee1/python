
fin  = open("lyrics.txt", "r")



lyrics = fin.readlines()

# print(lyrics)
fin.close()

lines = []

i =1
for line in lyrics:
    if 'piano man' in line:
        lines.append(i)
    i += 1




print("piano man in : ", lines)




