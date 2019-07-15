from functools import reduce
list =[2,2,3,4]
def mul(x,y):
	return x+y
print(reduce(mul,list,0))





total =reduce(lambda item, running_total: item + running_total, [1, 2, 3, 4, 5])
print(total)


words = ["hello", "world"]
def join_strings(strings):
	return reduce(lambda x,y: x + '' + y,strings)
print(join_strings(words))

