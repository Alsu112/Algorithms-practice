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


def add(memstruct, root, x, count, ans):
    key = memstruct[0][root][0]
    if x < key:
        left = memstruct[0][root][1]
        count += 1
        if left == -1:
            memstruct[0][root][1] = createandfillnode(memstruct, x)
            ans.append(count)
        else:
            add(memstruct, left, x, count, ans)
    elif x > key:
        right = memstruct[0][root][2]
        count += 1
        if right == -1:
            memstruct[0][root][2] = createandfillnode(memstruct, x)
            ans.append(count)
        else:
            add(memstruct, right, x, count, ans)


def traversal(root, memstruct):
    elem = root
    left = memstruct[0][elem][1]
    right = memstruct[0][elem][2]
    if left != -1:
        traversal(left, memstruct)
        # print(memstruct[0][left][0])
    print(memstruct[0][elem][0])
    if right != -1:
        traversal(right, memstruct)
        # print(memstruct[0][right][0])


numbers = list(map(int, input().split()))[:-1]
memstruct = initmemory(len(numbers))
root = createandfillnode(memstruct, numbers[0])
ans = [1]
for i in range(1, len(numbers)):
    add(memstruct, root, numbers[i], 1, ans)
traversal(root, memstruct)