# 모든 위치에서

# 모든 친구들의 거리를 계산해서

# 가장 적은 값을 알려주면 되겠죠!

# 1번 아이디어
# X, Y를 구분해서 계산해준 뒤에 합쳐서
# 최솟값을 알려주면 됩니다!

# 2번 아이디어
# 우리가 한 곳에서 모일 때, 비용을 최소화 하기 위해서는
# 우리의 집 중 한 곳에서 모이면 된다.
    
# 3번 아이디어
# 최소 거리를 계산하고 싶다.
# 그리고, 2명이 모여야한다.
# 그 점에서, 가까운 두 명의 거리만 더해주면 되지 않을까?

# A번짐 B번집 C번집

# [1,2,3] / [3,4,5] [2,2,5]

# 두 사람이 모일 수 있는 최소거리는 -> 3!
    
# for 반복문
# 입력과 출력
# 배열 list
# 정렬 sort

n = int(input())
arr = []
arr_y = []
arr_x = []
answer = [-1]*n

# 입력 받기
for _ in range(n):
    a,b = map(int,input().split())
    arr.append([a,b])
    arr_y.append(b)
    arr_x.append(a)

# 만날 장소 정하기
for y in arr_y:
    for x in arr_x:
        dist = []
        
        # 만날 장소로 각각의 점들이 오는 비용 계산하기
        for ex,ey in arr:
            d = abs(ex-x) + abs(ey-y)
            dist.append(d)

        
        # 가까운 순서대로 정렬하기
        dist.sort()

        tmp = 0 
        for i in range(len(dist)):
            d = dist[i]
            tmp += d
            if answer[i] == -1: 
                answer[i] = tmp
            else :
                answer[i] = min(tmp, answer[i])

print(*answer)


