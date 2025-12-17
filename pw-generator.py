import random

elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = int(input("Panjang password: "))
pw = ""

for i in range(length):
    pw += random.choice(elements)

print(pw)
