str = input("kor eng mat: ")
list = str.split()
# kor = int(list[0])
# eng = int(list[1])
# mat = int(list[2])
kor, eng, mat = list

#sum = int(kor) + int(eng) + int(mat)
kor, eng, mat = map(int, list)
sum = kor + eng + mat
average = sum / 3

print(f"sum : {sum} , average : {average:.2f} ")