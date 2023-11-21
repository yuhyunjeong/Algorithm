def recur(i):

    if i == m:
        print(*arr)
        return

    for j in range(1, n+1):
        if visited[j]:
            continue
        visited[j] = 1
        arr.append(j) # 
        recur(i+1)
        arr.pop() # 배열 비워줘야함
        visited[j] = 0


arr = []
n, m = map(int, input().split())
visited = [0 for _ in range(n+1)]

recur(0)
