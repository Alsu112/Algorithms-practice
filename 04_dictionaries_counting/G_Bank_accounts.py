import sys

def bank_accounts():
    dict_balance = {}
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        operation = list(line.split())
        if operation[0] == 'DEPOSIT':
            if operation[1] not in dict_balance:
                dict_balance[operation[1]] = int(operation[2])
            else:
                dict_balance[operation[1]] += int(operation[2])
        elif operation[0] == 'INCOME':
            for key in dict_balance:
                if dict_balance[key] > 0:
                    dict_balance[key] += int(int(operation[1]) * dict_balance[key] * 0.01)
        elif operation[0] == 'BALANCE':
            if operation[1] not in dict_balance:
                print('ERROR')
            else:
                print(dict_balance[operation[1]])
        elif operation[0] == 'TRANSFER':
            if operation[1] not in dict_balance:
                dict_balance[operation[1]] = 0
            if operation[2] not in dict_balance:
                dict_balance[operation[2]] = 0
            dict_balance[operation[1]] -= int(operation[3])
            dict_balance[operation[2]] += int(operation[3])
        elif operation[0] == 'WITHDRAW':
            if operation[1] not in dict_balance:
                dict_balance[operation[1]] = -1 * int(operation[2])
            else:
                dict_balance[operation[1]] -= int(operation[2])

if __name__ == "__main__":
    bank_accounts()
#O(N**2) по времени и O(N) по памяти