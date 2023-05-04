# fahr --> celsius
#fahr = 100
fahr = int(input("fahr : "))
celsius = 5 / 9 * (fahr - 32)
print("fahr : ", fahr, "celsius : ", celsius)
print("fahr : %d --->celsius : %.2f"%(fahr, celsius))
print("fahr : {:3d} ---> celsius : {:.2f}".format(fahr, celsius))
print(f"fahr : {fahr} ---> celsius : {celsius:.2f}")