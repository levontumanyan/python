arr1 = [ 1, 23, 42, 2, 4, 1, 5, 6, 7, 2, 213, 123]

def bubble_sort(arr):
	for i in range(len(arr)):
		#rint(i)
		#print(arr[i])
		for j in range(i+1, len(arr)):
			print(i,j)
			if (arr[i] > arr[j]):
				arr[i], arr[j] = arr[j], arr[i]
	return arr

print(bubble_sort(arr1))