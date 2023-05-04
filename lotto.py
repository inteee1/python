import random

# balls = []
# for i in range(1, 46):
#     balls.append(i)

balls = [i for i in range(1, 46)]

random.shuffle(balls)
lotto = balls[:7]

for ball in lotto:
    print(f"[{ball}] ", end="")
print()