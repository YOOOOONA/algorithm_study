from itertools import permutations,combinations
import sys
sys.stdin = open(".\\input.txt")
input = sys.stdin.readline

N = int(input())#단어개수
for _ in range(N):
    word = input().rstrip()
    a=sorted(list(set(permutations(word,len(word)))))
    for i in a:
        print(''.join(i))