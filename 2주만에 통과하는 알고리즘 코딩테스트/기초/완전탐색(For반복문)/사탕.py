candy = int(input())

# A >= B + 2
# A >= 1 , B >= 1, C >= 1
# C % 2 == 0

answer = 0

for A in range(0, candy+1): # 0 ~ 6개
    for B in range(0, candy+1): # 0 ~ 6개
        for C in range(0, candy+1): # 0 ~ 6개
            if A + B + C == candy:
                if A >= B + 2:
                    if A != 0 and B != 0 and C != 0:
                        if C % 2 ==0:
                            answer += 1

print(answer)

