def tinder():
	guys_who_have_swiped_us_right = ['Arjun','Abhimanyu','Rohan']
	list_of_guys = ['Rahul','Rohit','Arjun','Heeral','Manoj','Sidharth']
	for guy in list_of_guys:
		print(guy)
		x = input('Press R for Swiping Right, and L for Swiping Left')
		if x == 'R':
			if guy in guys_who_have_swiped_us_right:
				print('Congratulations!! Its a Match')