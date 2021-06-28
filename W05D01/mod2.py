List_of_movies = ['Phir Hera Pheri','Dhamaal','Golmaal','Welcome','Hungmama','Chupke chupke']

def netflix(movie):
	if movie in List_of_movies:
		print('Now Playing... ',movie)
	else:
		print(movie,' does not exist')

def tinder():
	profiles = ['Jitendera','Sharukh','Arjun','Rahul','Mayank']
	for profile in profiles:
		print(profile)
		z = input('Press R for Swiping Right or L for Swiping Left')
		if z=='R':
			print("Congratulations!!! It's a Match")
