"""
def only_odd_digits(n):
Check that the given positive integer n contains only odd digits (1, 3, 5, 7 and 9) when it is written out. Return True if this is the case, and False otherwise. Note that this question is not asking whether the number n itself is odd or even. You therefore will have to look at every digit of the given number before you can proclaim that the number contains no even digits.
To extract the lowest digit of a positive integer n, use the expression n%10. To chop off the lowest digit and keep the rest of the digits, use the expression n//10. Or, if you don’t want to be this fancy, you can 6irst convert the number into a string and whack it from there with string operations.
"""

def only_odd_digits_v1(n):
	
	while n != 0:
		if (n%2 == 0):
			return False
		else:
			n = n//10
	return True
		
def only_odd_digits_v2(n):
	for ch in str(n):
		if (int(ch) % 2 == 0):
			return False
	return True

print("Version 1")
print(only_odd_digits_v1(135))
print(only_odd_digits_v1(1357975313579))
print(only_odd_digits_v1(13579752512))
print(only_odd_digits_v1(134233))
print(only_odd_digits_v1(157935797))

print("Version 2")
print(only_odd_digits_v2(135))
print(only_odd_digits_v2(1357975313579))
print(only_odd_digits_v2(13579752512))
print(only_odd_digits_v2(134233))
print(only_odd_digits_v2(157935797))
