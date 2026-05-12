print("1: Feet to meter & 2: Meter to Feat")

choice = int(input("Enter Your Choice: "))


if choice ==  1:
    feet = int(input("Enter A Feat: "))
    meter = feet*0.304800
    print(meter," Meter")
    
elif choice == 2:
    meter = int(input("Enter Meter: "))
    feet = meter*3.28084
    print(feet," Feet")
