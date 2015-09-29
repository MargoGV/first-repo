A = [1, 2, 3, 4, 5]
A.insert(0, A.pop())
print(A)

for i in range(0, len(A)-1, 2):
    A[i], A[i+1] = A[i+1], A[i]
print(A)


A = [1, 2, 2, 2, 3, 3]
for i in range (len(A)):
    if A.count(A[i]) == 1:
        print(A[i])


