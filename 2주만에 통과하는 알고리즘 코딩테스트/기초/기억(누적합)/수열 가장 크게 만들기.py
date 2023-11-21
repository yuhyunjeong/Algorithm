# 다이나믹 프로그래밍 (메모이제이션)

import sys
input = sys.stdin.readline

n = int(input())

numbers = list(map(int,input().split()))
prefix = [-1001]*(n+1)

for i in range(n):
    prefix[i+1] = max(prefix[i] + numbers[i], numbers[i])


print(max(prefix))

