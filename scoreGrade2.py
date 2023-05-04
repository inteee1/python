GRADES = ['F', 'F', 'F', 'F', 'F', 'F', 'D', 'C', 'B', 'A']

score = int(input("score : "))

grade = GRADES[score//10]

print("score : ", score, "grade : ", grade)
