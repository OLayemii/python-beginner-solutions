def solution(A):
    if not all(x > 0 for x in A):
        return 1
    ans = sorted(list(set([x for x in range(1,sorted(A)[-1]+2)]) - set(A)))[0]
    return ans

print(solution([1,2,5]))