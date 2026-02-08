import sys

def count_unique_words():
    text = sys.stdin.read()
    words = text.split()
    unique_words = set(words)
    return len(unique_words)

print(count_unique_words())

#O(n) - временная сложность
#O(n) - пространственная сложность