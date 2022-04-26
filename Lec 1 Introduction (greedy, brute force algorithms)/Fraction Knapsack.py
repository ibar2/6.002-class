def fraction_knabsack(weight,profit,capacity):
	'''
		this is a greedy implementetion of fraction knapstack problem

	'''

	sor = sorted(zip(weight,profit), key = lambda x : x[1]/x[0], reverse= True)
	al = []
	res = 0
	for i in sor:
		if capacity:
			if i[0] > capacity:
				res += i[1] / (i[0] / capacity)
				al.append(f'{i[1]} but with  {i[1] / (i[0] / capacity)} profit')
				capacity = 0
			elif i[0] <= capacity:
				res+=int(i[1])
				al.append(i[1])
				capacity -= i[0]
	print(al)
	return f'maximum profit we could come out with is {res}'

weight = [24,10,4,1]
profit = [36,1,20,2]
limit = 25
print(fraction_knabsack(weight,profit,limit))