
a, b = map(int, input("input a b:").split())

try:
    result = a/b
    if b == 0:
        raise ZeroDivisionError("you can't divide by zero:")
    
    print(f"{a} / {b} = {result}")
except ZeroDivisionError as e:
    print(e)
    print("you can't divide by zero")