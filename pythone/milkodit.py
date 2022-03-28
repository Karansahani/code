milk = int(input("how many cm you have enter here "))

if milk > 120:
 print("lets go")
 age = int(input("what is your age "))
 if age <= 10:
     bill = 100
     print("tiket price is RS 100")
 elif age <= 20:
    bill = 180
    print("tiket price is RS 180")
 elif age <=25:
     bill = 250
     print("tiket price is RS 250")
 elif age >= 40 and age <= 70:
    print("don't wary you have goy free ride")

 else:
     bill = 500 
     print("tiket price is RS 500")
 you_want_photo = input("do you want photo Y or N")
 if you_want_photo == "Y":
  bill += 100
else:
  print("go back to your home")

print(f"your total bill is RS {bill}")