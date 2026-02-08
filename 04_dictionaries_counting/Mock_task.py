import sys
import re


def count_words_in_text_re():
    text = sys.stdin.read()
    pattern = re.compile(r'[,.;]')
    text = pattern.sub(' ', text).lower().strip().split()
    ans = set(text)
    print("re", ans)
    return len(ans)


original_stdin = sys.stdin

with open('input_mock.txt', 'r') as f:
    sys.stdin = f
    print(count_words_in_text_re())

sys.stdin = original_stdin