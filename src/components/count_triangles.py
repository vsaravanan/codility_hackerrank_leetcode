def count_triangles(A=[10, 2, 5, 1, 8, 20]):
    if len(A) < 3:
        return 0
    
    A.sort()
    count = 0
    print(A)
    for i in range(len(A) - 2):
        if A[i] >= 0 and A[i] + A[i + 1] > A[i + 2]:
            print(f"{A[i]} + {A[i + 1]} > {A[i + 2]}")
            count += 1
    
    return count

# Test the function
triangles_count = count_triangles()
print("Number of triangles:", triangles_count)
triangles_count =  count_triangles([3,4,7,1,5,6])
print("Number of triangles:", triangles_count)
