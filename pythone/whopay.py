import random


name = str(input("enter your name here all of you guys "))
lname = name.split(", ")
tseed = int(input("mix up your frind name enter 1  to  100  any of tham "))
random.seed(tseed)
x = len(lname)
r = random.randint(0 , x -1)

who = lname[r]


print(who + " you pay the bill")

