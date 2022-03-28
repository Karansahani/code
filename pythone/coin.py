import random

tseed = float(input("create your seed nunber"))
random.seed(tseed)

coin = random.randint(0 ,1)

if coin == 0:
    print("head")
else:
    print("tail") 