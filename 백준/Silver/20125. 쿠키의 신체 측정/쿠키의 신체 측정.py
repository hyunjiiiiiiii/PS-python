# 쿠키의 신체 측정

N = int(input())

idx_list = []
idx = 1

for _ in range(N):
    cookie = list(input())

    for i in cookie:
        if i == "*":
            idx_list.append(idx)
            idx += 1
        else:
            idx += 1

# print(cookie)
#print(idx_list)


# 심장
print(idx_list[0]//N + 2, idx_list[0]%N)
heart = idx_list[0] + N

# 왼팔, 오른팔, 허리, 왼쪽다리, 오른쪽다리
la = 0
ra = 0
b = 0
ll = 0
rl = 0
for i in range(len(idx_list)):

    if idx_list[i] == heart:
        la = i - 1
        
    
    if idx_list[i] == heart+N:
        ra = i - 2 - la

    if idx_list[i]%N == heart%N:
        # 머리, 심장 포함
        b += 1
        b_idx = i

ll_idx = b_idx + 1
rl_idx = b_idx + 2

# print(idx_list[ll_idx], idx_list[rl_idx])


for j in range(len(idx_list)):
    
    if j > b_idx and idx_list[j]%N == idx_list[ll_idx]%N:
        ll += 1

    if j > b_idx and idx_list[j]%N == idx_list[rl_idx]%N:
        rl += 1

print(la, ra, b-2, ll, rl)
