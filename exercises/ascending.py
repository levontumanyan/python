"""
def is_ascending_v1(items):
Determine whether the sequence of items is strictly ascending_v1 so that each element is strictly larger 
(not just merely equal to) than the element that precedes it.
Return True if the elements in the list of items are strictly ascending_v1, and return False otherwise.
Note that the empty sequence is ascending_v1, as is also every one-element sequence, so be careful to ensure
that your function returns the correct answers in these seemingly insigni6icant edge cases of this problem.
(If these sequences were not ascending_v1, pray tell, what would be the two elements that violate the requirement
and make that particular sequence not be ascending_v1?)
items
Expected result
[]
True
[-5, 10, 99, 123456]
True
[2, 3, 3, 4, 5]
False
[-99]
True
[4, 5, 6, 7, 3, 7, 9]
False
[1, 1, 1, 1]
False
In the same spirit, note how every possible universal claim made about 
the elements of an empty sequence is trivially true! For example, if items is the empty sequence, the two claims
“All elements of items are odd” and “All elements of items are even” are both equally true, as is also the claim
“All elements of items are colourless green ideas that sleep furiously.”
"""

def ascending_v1(sequence):
	if len(sequence) < 2:
		return True

	for i in range(len(sequence) - 1):
		if sequence[i] < sequence[i+1]:
			continue
		else:
			return False
	
	return True

def ascending_v2(sequence):
	if len(sequence) < 2:
		return True
	
	for i in range(len(sequence) - 1):
		if sequence[i] >=  sequence[i+1]:
			return False
	return True

	

print(ascending_v1([4, 5, 6, 7, 3, 7, 9]))
print(ascending_v1([-5, 10, 99, 123456]))
print(ascending_v1([]))
print(ascending_v1([4]))

print(ascending_v2([4, 5, 6, 7, 3, 7, 9]))
print(ascending_v2([-5, 10, 99, 123456]))
print(ascending_v2([]))
print(ascending_v2([4]))

