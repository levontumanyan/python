
"""2. Level 1: Write a program which can compute the factorial(recursively) of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

#Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

def rfactorial(num):

	if(num==1):
		return 1
	
	return num*rfactorial(num-1)


print(rfactorial(5))