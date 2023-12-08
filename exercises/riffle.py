"""
Riffle_v1 shuffle kerfuffle
def riffle_v1(items, out=True):
Given a list of items whose length is guaranteed to be even (note that “oddly” enough, zero is an even number), create and return a list produced by performing a perfect rif=le to the items by in- terleaving the items of the two halves of the list in an alternating fashion.
When performing a perfect rif6le shuf6le, also known as the Faro shuf6le, the list of items is split in two equal sized halves, either conceptually or in actuality. The 6irst two elements of the result are then the 6irst elements of those halves. The next two elements of the result are the second elements of those halves, followed by the third elements of those halves, and so on up to the last elements of those halves. The parameter out determines whether this function performs an out shuf6le or an in shuf6le that determines which half of the deck the alternating card is 6irst taken from.
"""

def riffle_v1(items, out=True):
	items1 = items[0:len(items)//2]
	items2 = items[len(items)//2:len(items)]
	result = []
	if out:
		for i in range(len(items)//2):
			result.append(items[i])
			result.append(items[i + len(items)//2])
	else:
		for i in range(len(items)//2):
			result.append(items[i + len(items)//2])
			result.append(items[i])
		
	return result

def riffle_v2(items, out=True):
	midpoint = len(items)//2
	first_half = items[:midpoint]
	second_half = items[midpoint:]

	result = [None]*(len(items))
	
	if out:
		result[::2] = first_half
		result[1::2] = second_half
	else:
		pass
	return result

print("Version 1")
print(riffle_v1([1,2,3,4]))
print(riffle_v1([1,2,3,4,123,23]))
print(riffle_v1([1,2,3,4,8,7]))
print(riffle_v1([1,2,3,4,12,34]))
print(riffle_v1([1, 2, 3, 4, 5, 6, 7, 8], False))

print("Version 2")
print(riffle_v2([1,2,3,4]))
print(riffle_v2([1,2,3,4,123,23]))
print(riffle_v2([1,2,3,4,8,7]))
print(riffle_v2([1,2,3,4,12,34]))
print(riffle_v2([1, 2, 3, 4, 5, 6, 7, 8], False))