numbers = [1,56,234,87,4,76,24,69,90,135]
def is_even(x):
	return (x%2 ==0)
print(list(map(is_even,numbers)))





def is_even(x):
        return (not x%2 ==0)
print(list(map(is_even,numbers)))


