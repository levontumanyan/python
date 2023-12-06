def five_adder(a):
	print(f"adding 5 to {a}:", end="")
	return a+5

def five_mult(a):
	print(f"multiplying {a} by 5", end=(""))
	return a*5

print(five_adder(6))
print(five_adder(1))
print(five_adder(5))

print(five_mult(6))
print(five_mult(2))
print(five_mult(3))
print(five_mult(4))
