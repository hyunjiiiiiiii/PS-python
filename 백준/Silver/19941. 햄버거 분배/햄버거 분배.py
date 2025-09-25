# 햄버거 분배
# import sys
# input = sys.stdin.readline

N, K = map(int, input().split())

H_list = list(input())

idx = 0
p_idx = []
while idx < N:
    if H_list[idx] == "P":
        p_idx.append(idx)
    
    idx += 1

cnt = 0
for i in p_idx:
    for j in range(i-K, i+K+1):
        if j >= N:
            break
        elif j < 0:
            continue
        
        elif H_list[j] == "H":
            H_list[j] = 1
            cnt += 1
            break

# print(H_list)
# print(p_idx)
print(cnt)