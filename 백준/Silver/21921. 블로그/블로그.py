# 블로그

import sys
input = sys.stdin.readline

N, X = map(int, input().split())

n_list = list(map(int, input().split()))


max_sum = sum(n_list[:X])
cnt = 1

curr_sum = max_sum
for i in range(1, N-X+1):
    
    curr_sum = curr_sum - n_list[i-1] + n_list[X+i-1]

    if curr_sum > max_sum:
        max_sum = curr_sum
        cnt = 1
    elif curr_sum == max_sum:
        cnt += 1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(cnt)
