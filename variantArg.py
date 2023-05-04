def my_sum(*args):
    total = 0
    print("args: ", args)
    for value in args:
        total += value
    return total

def my_sum(*args):      #redefine
    print("args: ", args)
    return sum(list(args))




n = 5
result = my_sum(n, 1, 2, 3, 4, 5) # 튜플(readonly)
print("result: ", result)