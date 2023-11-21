def solution(targets):
    answer = 0
    
    lst = []
    for x, y in targets:
        #print(x, y)
        #print(y-x)
        lst.append(y-x)
    
    print(lst)
    #print(sorted(lst))
    lst2 = sorted(lst)
    print(lst2)



    return answer

solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]])
