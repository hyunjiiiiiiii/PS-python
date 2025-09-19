# 크로스 컨트리

T = int(input())



for i in range(T):
    N = int(input())

    score_list = input().split()

    score_dic = {}
    for i in score_list:
        score_dic[i] = score_dic.get(i, 0) + 1

    # print(score_dic)
    # print(score_dic.values())

    parti = []
    rank = 1
    for j in score_list:    
        if score_dic[j] == 6:
            parti.append([int(j), rank])
            rank += 1
    
    #print(parti)
    parti.sort(key=lambda x: (x[0], x[1]))
    #print(parti)

    parti_idx = []
    for idx, (k, r) in enumerate(parti, start=1):
        parti_idx.append([idx, k, r])

    #print(parti_idx)

    parti_dic = {}
    for i, k, r in parti_idx:
        if i % 6 == 5 or i % 6 == 0:
            continue
        else:
            parti_dic[k] = parti_dic.get(k, 0) + r

    #print(parti_dic)

    min_val = min(parti_dic.values())
    winner = [k for k, v in parti_dic.items() if v == min_val]

    if len(winner) == 1:
        #print(winner)
        print(winner[0])
    else:
        fifth_rank = {}

        for i, k, r in parti_idx:
            if k in winner and i % 6 == 5:
                fifth_rank[k] = r
        
        winner = min(fifth_rank, key=fifth_rank.get)
        print(winner)
        

