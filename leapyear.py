def is_leap(year):
    leap = False

    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True

    return leap


try:
    year = (int)(input("Enter the year: "))
    if(is_leap(year)):  
        print("Leap year")  
    else:
        print("Not leap year")  
except ValueError:
    print("This is not a year. Try to run the program again.")


