year = int(input("which year you want to cheak leap year or not"))

if year % 4 == 0:
    if year%100==0:
        if year%400==0:
            print("yes is leap year")
        else:
         print("not leap year")

    else:
        print("Yes is leap year")
else:
    print("not leap year")