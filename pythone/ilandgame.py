print("welcome to treasure island your mission find the treasure ")
start = input ("do you start the game  Y , N ")
if start == "Y":
    print("ok")
else:
    print("ok thank you")


left = input("which way you want to go left  or  right")

if left == "right" :
    waitor = input("you reach the river your option  swim or  wait")
    if waitor == "swim":
        which1 = input("now you reach the island  now your option which door you want open  red  ,  blue  or green")
        if which1 == "blue":
         print ("you win the game 'GOOD JOB")
        elif which1 == "green":
         print("game over")
        else:
            print("game over")
    else:
        print("game over")
else:
    print("game over")