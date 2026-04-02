import sys
sys.setrecursionlimit(100000)

def initmemory(maxn):
  memory = []
  for i in range(maxn):
    memory.append([0, i + 1, []])
  return [memory, 0]

def newnode(memstruct):
  memory, firstfree = memstruct
  memstruct[1] = memory[firstfree][1]
  return firstfree

def createandfillnode(memstruct, key):
  index = newnode(memstruct)
  memstruct[0][index][0] = key
  memstruct[0][index][1] = -1
  memstruct[0][index][2] = []
  return index

def add(memstruct, index_parent, x):
  index_x = createandfillnode(memstruct, x)
  memstruct[0][index_parent][2].append(index_x)
  memstruct[0][index_x][1] = index_parent
  return index_x

def elem_number(root, memstruct, elem_number_dict):
  if root == -1:
    return 0
  num_elem = 0
  if len(memstruct[0][root][2]) != 0:
    for i in range(len(memstruct[0][root][2])):
      num_elem += 1
      if memstruct[0][root][2][i] in elem_number_dict:
        num_elem += elem_number_dict[memstruct[0][root][2][i]]
      else:
        num_elem += elem_number(memstruct[0][root][2][i], memstruct, elem_number_dict)
  elem_number_dict[root] = num_elem
  return num_elem

def depth_func(root, memstruct, depth_dict, depth = 0):
  if root == -1:
    return 0
  child_list = memstruct[0][root][2]
  if len(child_list) != 0:
    for i in range(len(child_list)):
      if child_list[i] in depth_dict:
        child_depth = depth_dict[child_list[i]]
      else:
        child_depth = depth_func(child_list[i], memstruct, depth_dict, depth + 1)
  depth_dict[root] = depth
  return depth

N = int(input())
root = ''
index_dict = {}
depth_dict = {}
memstruct = initmemory(N)
for i in range(N - 1):
  name, parent = input().split()
  if name in index_dict:
    index_name = index_dict[name]
  else:
    index_name = createandfillnode(memstruct, name)
    index_dict[name] = index_name
  if parent in index_dict:
    index_parent = index_dict[parent]
  else:
    index_parent = createandfillnode(memstruct, parent)
    index_dict[parent] = index_parent
  memstruct[0][index_name][1] = index_parent
  memstruct[0][index_parent][2].append(index_name)
sorted_list = sorted(index_dict.keys())
elem_number_dict = {}
for name, idx in index_dict.items():
    if memstruct[0][idx][1] == -1:
        root_index = idx
        break
root_depth = depth_func(root_index, memstruct, depth_dict)
for i in range(len(sorted_list)):
  print(sorted_list[i], depth_dict[index_dict[sorted_list[i]]])