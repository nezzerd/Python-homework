n = int(input())
d = dict()
for i in range(n):
    s = input()
    word1, word2 = s.split()
    d[word1] = word2
    d[word2] = word1
s = input()
print(d[s])
