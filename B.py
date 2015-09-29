A = [1, 2, 3, 4, 5]
A.insert(0, A.pop())
print(A)

for i in range(0, len(A)-1, 2):
    A[i], A[i+1] = A[i+1], A[i]
print(A)
