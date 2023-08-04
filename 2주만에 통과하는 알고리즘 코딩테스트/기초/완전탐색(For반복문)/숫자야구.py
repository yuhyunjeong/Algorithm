# A가 정답으로 생각할 수 있는 모든 수를 넣어보기!

# 그리고 B가 도전한 내용에 맞는지 확인하기!

n = int(input()) # 4

hint = [list(map(int, input().split())) for _ in range(4)]

# [[123,1,1],[356,1,0], ...]

answer = 0
# 100 ~ 999
for a in range(1,10): #100의 자리수
    for b in range(10): #10의 자리수
        for c in range(10): #1의 자리수

            if ( a == b and b == c and c == a ): 
                continue # 무시 
            
            # 다른 숫자로 이루어진 세 자리수

            # 숫자가 정해졌다면
            cnt = 0
            for arr in hint:
                number = hint[0]
                ball = hint[1]
                strike = hint[2]

                # a, b, c 라는 숫자
                # number 하고 비교해서

                # 자리수를 나눠서, strike ball 을 측정하는 부분

                ball_count = 0
                strike_count = 0

                if ball == ball_count and strike == strike_count:
                    cnt += 1
    
            if cnt == n:
                answer += 1

print(answer)


