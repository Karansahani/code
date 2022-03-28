print("welcome to love calculator")
name1 = input("what is your name \n")
name2 = input("what is their name \n")

combin = name1 + name2
lowerletter = combin.lower()

t = lowerletter.count("t")
r = lowerletter.count("r")
u = lowerletter.count("u")
e = lowerletter.count("e")

true = t + r + u + e

l = lowerletter.count("l")
o = lowerletter.count("o")
v = lowerletter.count("v")
e = lowerletter.count("e")

love = l + o + v + e

truelove = int(str(true) + str(love))

if truelove < 10 or truelove > 90:
    print("do not live together")
elif truelove >= 40 and truelove <= 50:
    print(f"your good to go together {truelove}")
else:
    print("good level love")
