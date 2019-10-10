import sys

def cut(rod_len, prices):
    cut_cache = [0 for _ in range(rod_len+1)]

    for i in range(1, rod_len+1):
        mx = float('-inf')
        for j in range(i):
            mx = max(mx, cut_cache[j] + prices[i-j-1])
        cut_cache[i] = mx
    return cut_cache[rod_len]

if __name__ == '__main__':
    num_cases = int(sys.stdin.readline().strip())

    for case_num in range(num_cases):
        rod_len = int(sys.stdin.readline().strip())
        prices = list(map(int, sys.stdin.readline().strip().split(' ')))

        print(cut(rod_len, prices))
