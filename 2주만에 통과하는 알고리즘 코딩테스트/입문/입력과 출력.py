# 입력을 받고 (디테일!)

# Default input 스트링 타입, 문자열 타입으로 받아와주도록 만들어짐!

# 배열 !
# list = [0,0,0,0]
# list = ["he","hi","hu"]


# Case 1 : 단순히 정수 일 때,
#number = int(input())

# Case 2 : 수열
list1 = list(map(int, input().split()))
print(list1)
print(*list1) #원소만 출력


# Case 3 : 단순히 문자 일 때,
#string = input()

# Case 4 : 문자열
list2 = list(map(str, input().split()))
print(list2)
print(*list2) #원소만 출력


# 계산을 하고

# 출력을 한다
#print(number + number)
#print(string + string)
