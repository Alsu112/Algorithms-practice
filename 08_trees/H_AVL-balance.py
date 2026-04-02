def initmemory(maxn):
    memory = []
    for i in range(maxn):
        memory.append([0, i + 1, 0])
    return [memory, 0]


def newnode(memstruct):
    memory, firstfree = memstruct
    memstruct[1] = memory[firstfree][1]
    return firstfree


def createandfillnode(memstruct, key):
    index = newnode(memstruct)
    memstruct[0][index][0] = key
    memstruct[0][index][1] = -1
    memstruct[0][index][2] = -1
    return index


def add(memstruct, root, x):
    key = memstruct[0][root][0]
    if x < key:
        left = memstruct[0][root][1]
        if left == -1:
            memstruct[0][root][1] = createandfillnode(memstruct, x)
        else:
            add(memstruct, left, x)
    elif x > key:
        right = memstruct[0][root][2]
        if right == -1:
            memstruct[0][root][2] = createandfillnode(memstruct, x)
        else:
            add(memstruct, right, x)


def height(root, memstruct):
    if root == -1:
        return 0
    left = memstruct[0][root][1]
    right = memstruct[0][root][2]
    left_height = height(left, memstruct)
    right_height = height(right, memstruct)
    return max(left_height, right_height) + 1


def traversal(root, memstruct):
    count = 0
    count_all = 0
    elem = root
    left = memstruct[0][elem][1]
    right = memstruct[0][elem][2]
    if left != -1:
        count_left, count_all_left = traversal(left, memstruct)
        count += count_left
        count_all += count_all_left
    if abs(height(left, memstruct) - height(right, memstruct)) <= 1:
        count += 1
    count_all += 1
    if right != -1:
        count_right, count_all_right = traversal(right, memstruct)
        count += count_right
        count_all += count_all_right
    return count, count_all


numbers = list(map(int, input().split()))[:-1]
memstruct = initmemory(len(numbers))
root = createandfillnode(memstruct, numbers[0])
for i in range(1, len(numbers)):
    add(memstruct, root, numbers[i])
count, count_all = traversal(root, memstruct)
if count == count_all:
    print("YES")
else:
    print("NO")