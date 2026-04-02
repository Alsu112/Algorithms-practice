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


def second_maximum(root, memstruct):
    elem = root
    next_elem = memstruct[0][elem][2]
    if next_elem == -1:
        next_elem = memstruct[0][elem][1]
        while memstruct[0][next_elem][2] != -1:
            elem = next_elem
            next_elem = memstruct[0][elem][2]
        return memstruct[0][next_elem][0]
    while memstruct[0][next_elem][2] != -1:
        elem = next_elem
        next_elem = memstruct[0][elem][2]
    if memstruct[0][next_elem][1] != -1:
        next_elem = memstruct[0][next_elem][1]
        while memstruct[0][next_elem][2] != -1:
            elem = next_elem
            next_elem = memstruct[0][elem][2]
        return memstruct[0][next_elem][0]
    else:
        return memstruct[0][elem][0]


numbers = list(map(int, input().split()))[:-1]
memstruct = initmemory(len(numbers))
root = createandfillnode(memstruct, numbers[0])
ans = [1]
for i in range(1, len(numbers)):
    add(memstruct, root, numbers[i], 1, ans)
print(second_maximum(root, memstruct))