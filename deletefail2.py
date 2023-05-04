import random



def isPass(score):
    return score >= 60



scores = [random.randint(0, 100) for _ in range(1, 15+1)]
print("scores: ", scores)

result = list(filter(isPass,scores))

print("result: ", result)