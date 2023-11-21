# 완전탐색
# 정수론( 공약수 )

# 두 수를 비교해서 최대공약수가 1이라면 OK
# 두 수를 비교해서 최대공약수가 1이 아니라면 NOK

# 숫자를 하나 추가하거나
# 또는 두 개 추가한다.
# (세 개 이상 필요없음. 귀납법으로 증명 가능)

for i in range(42, 2184):
    if gcd(42, i) == 1:
        if gcd(2184, i) == 1:
            coumt += 1
            break

for j in range(2184, 2200):
    if gcd(42, i) == 1:
        if gcd(2184, i) == 1:
            coumt += 1
            break
    if j == 2199:
        count += 2