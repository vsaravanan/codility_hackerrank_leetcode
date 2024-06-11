def solution(A, B):
    if len(A) == 0:
        return 0

    count = 1
    prev_end = B[0]

    for i in range(1, len(A)):
        print(count, prev_end)
        if A[i] > prev_end:
            count += 1
            prev_end = B[i]

    print(count, prev_end)
    return count

a = solution([1, 3, 7, 9, 9], [5, 6, 8, 9, 10])
print(a)