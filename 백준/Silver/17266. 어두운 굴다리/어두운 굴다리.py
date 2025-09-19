# 어두운 굴다리
import math

# 굴다리 길이
N = int(input())

# 가로등 길이
M = int(input())

# 가로등 위치
x = list(map(int, input().split()))

bw = []
if len(x) > 1:
    for i in range(0, len(x)-1):
        bw.append(math.ceil((x[i+1] - x[i])/2))

bw.append(x[0] - 0)
bw.append(N - x[-1])

#print(bw)
print(max(bw))