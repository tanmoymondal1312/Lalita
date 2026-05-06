year = 800

# if(year%4==0):
#     print(year, "is a leap year.")

if (year%100 != 0 and year % 4 == 0) or year % 400 == 0:
    print("Yes Its a Leap Year **************")
else:
    print("Its not leap year")