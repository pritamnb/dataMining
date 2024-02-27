
def leapYearCheck(year):
    if ((year % 4 == 0) or (year % 100 != 0) and (year % 400 == 0) or (year % 3200 == 0)) :
        return 'it is a leap year!'
    else :  
        return 'A common year!'

print('Please enter a year')
yearInput = input()
year = int(yearInput)
print('Entered year', year)
yearType = leapYearCheck(year)
print('Year type : ', yearType)

