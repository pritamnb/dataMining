
def iso_day_of_week(date, month, year):
	isDateValid = validate(date, month, year)
	iso_day_of_week(date, month, year) if isDateValid['code'] == "true " else print(isDateValid['status']) 
	print(isDateValid['status'])

	m = int(month)
	q = int(date)
	y = int(year)
	if m < 3:
		m = m + 12
		y = y - 1
	k = y % 100
	j = y // 100
	
	h = (q + ((13*(m + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)) % 7
	print("h",h)
	d = ["Saturday","Sunday","Monday", "Tuesday", "Wednesday","Thursday","Friday" ]

	return d[((h+5)%7)+1]

def validate(date, month, year):
	if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
		max_day_value = 31
	elif month == 4 or month == 6 or month == 9 or month == 11:
		max_day_value = 30
	elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
		max_day_value = 29
	else:
		max_day_value = 28

	if month < 1 or month > 12:
		return { "status":"Invalid Date", "code": "false" }
	elif date < 1 or date > max_day_value:
		return { "status":"Invalid Date", "code": "false" }
	else:
		return { "status":"Valid Date", "code": "true" }
	
# date = input("Please enter a date")
# month = input("Please enter a month")
# year = input("Please enter a year")
print(iso_day_of_week(27, 2, 2024))