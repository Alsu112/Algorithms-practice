def higher_neighbours():
	input_list = list(map(int, input().split()))
	ans = 0
	for i in range(1, len(input_list) - 1):
		if input_list[i] > input_list[i-1] and input_list[i] > input_list[i+1]:
			ans += 1
	return ans
print(higher_neighbours())