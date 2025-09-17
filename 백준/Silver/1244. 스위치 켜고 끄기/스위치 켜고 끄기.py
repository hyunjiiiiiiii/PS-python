# 스위치 켜고 끄기

S = int(input())

s_list = list(map(int, input().split()))

N = int(input())

def change(b):
    if b == 1:
        return 0
    else:
        return 1

for i in range(N):
    A, B = map(int, input().split())

    if A == 1:
            mul = 1
            b = B
            while b <= S:
                s_list[b-1] = change(s_list[b-1])
                mul += 1
                b = B*mul


        
    if A == 2:

        mi = 1
        b = B-1

        s_list[b] = change(s_list[b])

        while (b-mi)>=0 and (b+mi)<S and s_list[b-mi] == s_list[b+mi]:
            s_list[b-mi] = change(s_list[b-mi])
            s_list[b+mi] = change(s_list[b+mi])
            mi += 1
            

    #print(s_list)


for i in range(len(s_list)):
    print(s_list[i], end=' ')
    if (i+1) % 20 == 0:
        print()
