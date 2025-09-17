# 등수 구하기

N, S, P = map(int, input().split())

if N == 0:
    print(1)
    exit()

score_list = list(map(int, input().split()))
# print(score_list)

rank = 1
idx = 1
same = 0
for i in score_list:

    if i > S:
        rank += 1
        idx += 1
    elif i == S:
        same += 1
    else:
        break

#print(idx+same, rank)

if idx+same > P:
    print(-1)
else:
    print(rank)

