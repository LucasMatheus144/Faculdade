from random import randint
A = [0]*10
for k in range(0,10):
    A[k] = randint(0,15)
print(A)
for k in range(0,10):
    for j in range(k+1,10):
        if A[j] < A[k]:
            A[j], A[k] =A[k], A[j]
print(A)