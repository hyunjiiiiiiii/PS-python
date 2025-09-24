# 영단어 암기는 어려워
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

words_dict = {}
for i in range(N):
    word = input().strip()
    if len(word) >= M:
        words_dict[word] = words_dict.get(word, 0) + 1

# tuple
words_list = list(words_dict.items())

# list
# words_list = [[k, v] for k, v in words_dict.items()]

# for l in range(len(words_list)):
#     words_list[l][1] = (-words_list[l][1])
#     words_list[l].append(-len(words_list[l][0]))

# print(words_list)

# 오름차순
words_list.sort(key=lambda x : (-x[1], -len(x[0]), x[0]))
    
for p in words_list:
    print(p[0])


