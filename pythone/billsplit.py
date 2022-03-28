persion = int(input("howmouch friend you have"))
bill = float(input("howmouch of your total bill "))
tipp  = int(input("howmouch you pay tipp in %  10 12 16 20 and 25 "))

total = bill /100 * tipp + bill / persion

ftotal = round(total , 2)
print("pay ", ftotal , " each friend ")