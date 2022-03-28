import random



user = input("rock , paper , sessior ,    any of tham ")
game = ["rock", "paper", "sessior"]


game1 = random.randint(0 , 2)

x = game[game1]

  

print(f"{user}\n {x}")

if user == "rock":
    ix = 0
if user == "paper":
    ix = 1
if user == "sessior":
    ix = 2

if ix == 0 and game1 == 2:
    print("win")
elif game1 == 0 and ix == 2:
    print("loss")
elif ix > game1:
    print("win")
elif game1 > ix :
    print("loss")
elif game1 == ix:
    print("draw ")
else:
    print("loss")