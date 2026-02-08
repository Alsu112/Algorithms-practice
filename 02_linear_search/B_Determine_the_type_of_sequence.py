import sys


def sequence_type():
    nums = []
    for line in sys.stdin:
        num = int(line.strip())
        if num == -2000000000:
            break
        nums.append(num)

    if len(nums) == 0:
        return 'RANDOM'
    if len(nums) == 1:
        return 'CONSTANT'

    d = {'CONSTANT': 0, 'ASCENDING': 0, 'WEAKLY ASCENDING': 0, 'DESCENDING': 0, 'WEAKLY DESCENDING': 0}

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            d['CONSTANT'] += 1
        if nums[i] < nums[i + 1]:
            d['ASCENDING'] += 1
        if nums[i] <= nums[i + 1]:
            d['WEAKLY ASCENDING'] += 1
        if nums[i] > nums[i + 1]:
            d['DESCENDING'] += 1
        if nums[i] >= nums[i + 1]:
            d['WEAKLY DESCENDING'] += 1

    for key, value in d.items():
        if d[key] == len(nums) - 1:
            return key
    return 'RANDOM'


print(sequence_type())