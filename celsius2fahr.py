celsius = int(input("celsius : "))
fahr = (celsius * 9 / 5) + 32
print("celsius : ", celsius, "fahr : ", fahr)
print("celsius  : %d --->celsius : %.2f"%(celsius , fahr))
print("celsius  : {:3d} ---> celsius : {:.2f}".format(celsius , fahr))
print(f"celsius  : {celsius } ---> celsius : {fahr:.2f}")