def binary_search():
    def check_function(m, params):
        k, nums = params
        return nums[m] >= k

    def lbin_search(left, right, check_function, check_params):
        while left < right:
            middle = (left + right) // 2
            if check_function(middle, check_params):
                right = middle
            else:
                left = middle + 1
        return left

    N, K = map(int, input().split())
    N_list = list(map(int, input().split()))
    K_list = list(map(int, input().split()))
    for k in K_list:
        if lbin_search(0, N, check_function, (k, N_list)) <= N - 1 and k == N_list[
            lbin_search(0, N, check_function, (k, N_list))]:
            print("YES")
        else:
            print("NO")


binary_search()