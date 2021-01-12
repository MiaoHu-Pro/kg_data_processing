
import numpy as np

a = np.random.random_integers(0,5-1)

print(a)



A = [
    [1,2,3],
    [1,0,3],
    [1,5,3],
    [1,2,1],
    [1,2,1],
    [0,1,3]

]

A = np.array(A)

print(A.shape)
h = 1
t = 3

for x in range(len(A)):
    if h == A[x][0] and t == A[x][2]:
        print(A[x],A[x][1])

h_data = list(A[:,0])
t_data = list(A[:,2])

print(h_data)
print(t_data)

index_h = [i for i, x in enumerate(h_data) if x == h]
index_t = [i for i, x in enumerate(t_data) if x == t]

retA = [i for i in index_h if i in index_t]
print(retA)









print()




