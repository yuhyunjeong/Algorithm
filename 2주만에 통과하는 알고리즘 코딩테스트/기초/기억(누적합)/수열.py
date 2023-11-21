a, b = map(int,input().split())

array = list(map(int,input().split()))

prefix = [0 for _ in range(a+2)] # 1칸 더 크게 만들기!

for i in range(0,a):
    prefix[i+1] = prefix[i] + array[i]

answer = []
for k in range(b,a+1):
    answer.append(prefix[k] - prefix[k-b])
   
print(max(answer))
