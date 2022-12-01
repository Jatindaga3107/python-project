# Creating a function to verify date format

import datetime

def date_checker(date):
    try:
        datetime.datetime.strptime(date, '%d/%m/%Y')
        return True
    except ValueError:
        return False
    

# Asking user to input date in dd/mm/yyyy format

print("Enter the range of dates in the format dd/mm/yyyy")

# taking the starting year and validating the fromat
# if the format is not correct then the program will ask for the input again

a = " "
while date_checker(a) == False:
    a = input("Enter the starting year: ")
    if date_checker(a) == False:
        print("Enter the date in the correct format")     

         
#  checking if the ending year is greater than the starting year
def verify_date(a,b):
    if b >= a:
        return True
    else:
        return False
    
# taking the ending year and validating the format
# if the format is not correct then the program will ask for the input again
    
b = " "
while date_checker(b) == False or verify_date(a,b) == False:
    b = input("Enter the ending year: ")
    if date_checker(b) == False:
        print("Enter the date in the correct format")
    if int(a[-4:]) > int(b[-4:]):
        print("The starting year should be less than the ending year")
           

# printing of leap years and non leap years

a = int(a[-4:])
b = int(b[-4:])
print("Leap years are: ")
for i in range(a,b+1):
    if i%4==0:
        print(i, end=" ")
print()
print("Non leap years are: ")
for i in range(a,b+1):
    if i%4!=0:
        print(i, end=" ")

