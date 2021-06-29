def filter_list(test_list):
	even = []
	odd = []
	for i in test_list:
		if i%2==0:
			even.append(i)
		else:
			odd.append(i)
	print(even)
	print(odd)