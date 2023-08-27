# 1978, #11653, #14232

n = int(input())

for i in range(1, int(n**0.5)+1): # 약수를 구할때는 해당 값의 루트를 알면 된다
    if n % i == 0:
        print(i, n//i)