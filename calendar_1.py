# To accept a valid month

while True:
	try:
		mm = int(input("Enter a month: "))
	except ValueError:
		print("Sorry, I didn't understand that.")
		continue
	if mm < 1 or mm > 12:
		print("Invalid Date!")
	else:
		break
# To accept a valid year
while True:
	try:
		yy = int(input("Enter a year: "))
	except ValueError:
		print("Sorry, I didn't understand that.")
		continue
	if yy < 1 or yy > 3000:
		print("Invalid year!")
	else:
		break

def calendar(mm,yy):
	mm = int(mm)
	yy = int(yy)
	if mm < 1 or mm > 12:
		return	print("Invalid Date")
	
	nly =[31, 28, 31, 30, 31, 30,
		31, 31, 30, 31, 30, 31]
	
	# leap year array
	ly =[31, 29, 31, 30, 31, 30,
		31, 31, 30, 31, 30, 31]
	
	# start of the day out of 365 or 366
	s = 0

	month ={1:'January', 2:'February', 3:'March',
			4:'April', 5:'May', 6:'June', 7:'July',
			8:'August', 9:'September', 10:'October',
			11:'November', 12:'December'}

	# odd days
	day = (yy-1)% 400
	day = (day//100)*5 + ((day % 100) - (day % 100)//4) + ((day % 100)//4)*2
	day = day % 7


	if yy % 4 == 0:
		for i in range(mm-1):
			s+= ly[i]
	else:
		for i in range(mm-1):
			s+= nly[i]
	day += s % 7
	day = day % 7

	space =''
	space = space.rjust(2, ' ')
	print()
	print(month[mm], yy)
	print('Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa')

	if mm == 9 or mm == 4 or mm == 6 or mm == 11:
		for i in range(31 + day):

			if i<= day:
				if(day == 6):
					print('', end ='') 
				else:
					print(space, end =' ')
			else:
				print("{:02d}".format(i-day), end =' ')
				if (i + 1)% 7 == 0:
					print()
	elif mm == 2:
		if yy % 4 == 0:
			p = 30
		else:
			p = 29

		for i in range(p + day):

			if i<= day:
				print(space, end =' ')
			else:
				print("{:02d}".format(i-day), end =' ')
				if (i + 1)% 7 == 0:
					print()
	else:
		
		for i in range(32 + day):
			
			if i<= day:
				if(day == 6):
					print('', end ='') 
				else:
					print(space, end =' ')
				
			else:
				print("{:02d}".format(i-day), end =' ')
				if (i + 1)% 7 == 0:
					print()

# User input
calendar(mm,yy)

# For static values uncomment the following code

# calendar(1,2024)
# calendar(2,2024)
# calendar(3,2024)
# calendar(4,2024)
# calendar(5,2024)
# calendar(6,2024)
# calendar(7,2024)
# calendar(8,2024)
# calendar(9,2024)
# calendar(10,2024)
# calendar(11,2024)
# calendar(12,2024)




