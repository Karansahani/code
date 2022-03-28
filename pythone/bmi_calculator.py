hight  = float(input("what is your hihht in foot"))

wieght = int(input("what is your wieght"))

bmi =round(wieght / hight ** 2 ,2)

if bmi <= 18.5:
    print(f"you are {bmi} underweight")
elif bmi <=25:
    print(f"you are {bmi} normal weight")
elif bmi <=30:
    print(f"you are {bmi} overweight")
elif bmi <=35:
    print(f"you are {bmi} obese")
else:
    print(f"you are {bmi} clinically obese")