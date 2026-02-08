import sys


def checking_cheating():
    def split_by_delimiters(text, key_words, C, D):
        delimiters = set(' \t\n\r+-*/=<>!&|^~%.,:;?()[]{}"\'`#@$\\')
        digits = set('1234567890')
        tokens = {}
        current = []
        exist_letter = False
        first_appearance = {}
        position = 0

        for char in text:
            if char in delimiters:
                if current:
                    if ''.join(current) not in key_words and (
                            D == 'yes' or ''.join(current)[0] not in digits) and exist_letter != False:
                        if ''.join(current) not in tokens:
                            tokens[''.join(current)] = 1
                            first_appearance[''.join(current)] = position
                        else:
                            tokens[''.join(current)] += 1
                    current = []
                    exist_letter = False
            else:
                if char not in digits:
                    exist_letter = True
                if C == 'no':
                    current.append(char.lower())
                else:
                    current.append(char)
            position += 1

        if current:
            if ''.join(current) not in key_words and (
                    D == 'yes' or ''.join(current)[0] not in digits) and exist_letter != False:
                if ''.join(current) not in tokens:
                    tokens[''.join(current)] = 1
                    first_appearance[''.join(current)] = position
                else:
                    tokens[''.join(current)] += 1

        return tokens, first_appearance

    first_row = list(input().split())
    N = int(first_row[0])
    C = first_row[1]
    D = first_row[2]
    key_words = set()

    for i in range(N):
        if C == 'no':
            key_words.add(input().lower())
        else:
            key_words.add(input())

    input_data = sys.stdin.read()
    counter, first_appearance = split_by_delimiters(input_data, key_words, C, D)

    max_value = float('-inf')
    min_position = float('inf')
    ans = ''

    for key in counter:
        if counter[key] > max_value:
            max_value = counter[key]
            min_position = first_appearance[key]
            ans = key
        elif counter[key] == max_value and first_appearance[key] < min_position:
            min_position = first_appearance[key]
            ans = key

    return ans


print(checking_cheating())
# O(S) по времени и по памяти, где S - длина текста