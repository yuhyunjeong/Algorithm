import sys
sys.setrecursionlimit(9999999) # 파이썬은 재귀함수를 1000번 정도 반복하면 멈추므로 의도적으로 크게 해서 방지.


def recur(hint_idx, number):
    if hint_idx == 4:
        answer += 1
        recur(0, number+1)
        return
    
    if number == 1000:
        return
    
    # 만약에 힌트를 통과했다면
    if # 스트라이크 카운트랑 볼 카운트가 동일하다면,
        recur(hint_idx+1, number)

    if # 만약에 힌트를 통과하지 않았다면
        recur(0, number+1)

