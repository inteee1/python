import re
fin = open('lyrics.txt', 'r')
lines = fin.readlines()
fin.close()

wordCount = {}

for index, line in enumerate(lines):
    words = line.strip().split()
   
    for word in words:
        word = re.sub(r"[^0-9a-zA-Z\s]", "", str(word))
        if word not in wordCount.keys():
            wordCount[word] = [index]
        else:
            wordCount[word].append(index)
for word, lines in wordCount.items():
    print(word, ":" , lines)

# for index, line in enumerate(lines):
#     words = line.strip().split()
#     for word in words:
#         word = word.strip('", ()').lower()
#         if word not in wordCount.keys():
#             wordCount[word] = [index]
#         else:
#             wordCount[word].append(index)

# for word, lines in wordCount.items():
#     print(word, ":" , lines)
