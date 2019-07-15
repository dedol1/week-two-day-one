#sentence = "the quick brown fox jumps over the lazy dog"
#words = sentence.split()
#print(words)


#new = [len(word) for word in words]
#print(new)


#q = [len(word) for word in words if word != "the"]
#print(q)

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
def positive_num(x):
	return x > 0
print(list(filter(positive_num,numbers)))


numb = [12, 54, 33, 67, 24, 89, 11, 24, 47]
def even(x):
	return (x%2 ==0)
print(list(filter(even,numb)))

