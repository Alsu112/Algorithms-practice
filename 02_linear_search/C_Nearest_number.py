def nearest_number():
	N = int(input())
	list_numbers = list(map(int, input().split()))
	x = int(input())
	ans = list_numbers[0]
	for elem in list_numbers:
		if abs(elem - x) < abs(ans - x):
			ans = elem
	return ans

print(nearest_number())