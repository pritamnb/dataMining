def leapYearCheck(year):
    if ((year % 4 == 0) or (year % 100 != 0) and (year % 400 == 0) or (year % 3200 == 0)):
        return {
            'status': True,
            'message' : 'it is a leap year!'
        }
    else:
        return {
            'status': False,
            'message' :'A common year!'
        }

# This is for only required function should get called in other files.
    # leapYearCheck is getting called in day_of_the_week.py
    # If condition resist the execution of code within main, when leapYearCheck gets called from other file
if __name__ == "__main__":
    print('Please enter a year !!!')
    yearInput = input()
    year = int(yearInput)
    print('Entered year', year)
    yearType = leapYearCheck(year)
    print('Year type : ', yearType['message'])
