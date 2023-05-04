import random

def deleteFail(scores):
    for data in scores:
        if data < 60:
            scores.remove(data)

scores = []

for _ in range(1, 15+1):
    scores.append(random.randint(0, 100))
print("scores: ", scores)
deleteFail(scores)
print("scores: ", scores)