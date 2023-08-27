# 1. 갭을 줄여도 된다!

# 8 12
# 4 8

# 2. 최대 공약수라는 말은 두 수 중 하나로 나누어서 나머지가 생기지 않는다는 말이다

# 8 4
# 최대공약수

# 3. 한 수를 가능한 만큼 갭을 줄인다.
# 하나의 수를 작은 수로 되는 만큼 뺀다는 말은
# 나누고 나서 나머지를 뜻한다!

# 121 7
# 121-7-7-7-7-7-7-7
# 121%7

A, B = map(int, input().split())

# 최대공약수
def _gcd(a, b): 
    while a % b != 0: # 나머지가 0이 되는 순간 멈춘다.
        tmp = a % b
        a = b
        b = tmp
    return b

# 최소공배수
def _lcm(a, b):
    return a * b // _gcd(a, b) # 두 수 곱하고 최대공약수로 나누기

gcd = _gcd(A,B)
lcm = _lcm(A,B)

maxg = gcd*lcm
answer = []

for i in range(gcd, int(maxg**0.5) + 1, gcd):
    if _gcd(i, (maxg//i)) == gcd:
        if _lcm(i, (maxg//i)) == lcm:
            answer.append((i,maxg//i))

print(answer)
print(*answer[0])
print(gcd, lcm)
#print(_gcd(A,B) , _lcm(A,B))