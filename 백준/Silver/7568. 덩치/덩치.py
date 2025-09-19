# 덩치

N = int(input())

rank_list = []
for i in range(N):
    rank_list.append(list(map(int, input().split())))

for j in range(N):
    rank = 1
    for k in range(N):
        if rank_list[j][0] < rank_list[k][0] and rank_list[j][1] < rank_list[k][1]:
            rank += 1
    rank_list[j].append(rank)

# print(rank_list)


print(" ".join(str(rank_list[_][2]) for _ in range(N)))