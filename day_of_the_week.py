from  leap_year import leapYearCheck
def iso_day_of_week(date, month, year):
    m = int(month)
    q = int(date)
    y = int(year)
    if m < 3:
        m = m + 12
        y = y - 1
    k = y % 100
    j = y // 100

    h = (q + ((13 * (m + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)) % 7
    d = [ "Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    isoDay = ((h + 5) % 7) + 1
    return d[isoDay]


def validate(date, month, year):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        max_day_value = 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        max_day_value = 30
    # elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    # Using a function from leap year
    elif (leapYearCheck(year)['status'] == True):
        max_day_value = 29
    else:
        max_day_value = 28

    if month < 1 or month > 12:
        return {"message": "Invalid Date", "status": False}
    elif date < 1 or date > max_day_value:
        return {"message": "Invalid Date", "status": False}
    else:
        return {"message": "Valid Date", "status": True}

# For Run time user input please uncomment the following code
# date = input("Please enter a date")
# month = input("Please enter a month")
# year = input("Please enter a year")

# 22/02/2024 - 22nd february 2024
# date = 22
# month = 2
# year = 2024

isDateValid = validate(date, month, year)
print('Is date valid ? ', isDateValid['message'])
day = iso_day_of_week(date, month, year) if isDateValid['status'] == True else print(isDateValid['message'])
print('Day is ', day)