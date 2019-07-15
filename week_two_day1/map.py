def area(r):
	return 3.14*(r*r)
radii =[2,3,4]
mp = map(area,radii)
print(list(mp))


num = [-1,0,1,2,3]
def bool(y):

	if y > 0:
		return True
print(list(filter(bool,num)))
