import random

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

question = random.sample(list, 3)
print("question: ", question)
strike = 0
ball = 0
count = 0
while strike != 3:
    strkie = ball = 0
    
    # a, b, c = map(int, input("a b c : ").split())
    # answer = [a, b, c]
    # 
    
    answer = list(map(int, input("a, b, c : ")).split())
    print("answer : ", answer)
    # answer = list(t)

    for i in range(0, 3):
        for j in range(0, 3):
            if question[i] == answer[j]:
                if i == j:
                    strike += 1
                else:
                    ball += 1
    print("strike : ", strike, "ball : ", ball)
    count += 1

print("congraturation! your count : ", count)