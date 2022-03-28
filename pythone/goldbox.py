row1 = ["@", "@", "@"]
row2 = ["@", "@", "@"]
row3 = ["@", "@", "@"]


map = [row1, row2, row3]

print(f"{row1}\n {row2}\n {row3}")

place = (input("which box you want to fill enter index number "))

user =input("enter O  or X ")

vertical = int(place[0])
horizontal = int(place[1])

finalmap = map[vertical -1]

finalmap[horizontal -1] =  user

print(f"{row1}\n {row2}\n {row3}")