### bitwise or

def bitwise_or(a, b):
	print(bin(a))
	print(bin(b))
	print(bin(a|b))
	print(a|b)

bitwise_or(45, 34)

### bitwise and

def bitwise_and(a, b):
	print(bin(a))
	print(bin(b))
	print(bin(a&b))
	print(a&b)

bitwise_and(45, 34)
bitwise_and(45, 34332)
bitwise_and(32223, 1)

### bitwise right shift
def bitwise_right_shift(a, b):
	print(bin(a))
	print(b)
	print(bin(a>>b))
	print(a>>b)

bitwise_right_shift(45, 2)

### is number even
def is_odd(num):
	if num & 1:
		return True
	else:
		return False
	
print(is_odd(423))
print(is_odd(42312))
print(is_odd(42341))
print(is_odd(42322))
print(is_odd(42))

### count set bits

def count_set_bits(num):
	og_num = num
	count = 0

	while num > 0:
		if num & 1:
			count += 1
			num >>= 1
		else:
			num >>= 1
		
	return(f'Num is: {og_num}, in binary: {bin(og_num)} and has {count} many digits set as 1')



print(count_set_bits(21312))