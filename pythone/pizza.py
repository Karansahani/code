print ("welcom to our pizza nut")

size = input("what size pizza you want S , M and L")
pepperoni =input("do you want pepperoni say Y , N")
extracheese = input("do you want extra cheese Y , N ")
bill= 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("choose right size please")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extracheese == "Y":
  bill += 1

print (f"your total bill $ {bill}")
