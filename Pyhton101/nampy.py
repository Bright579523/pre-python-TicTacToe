import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a)

print(a.ndim)

b = np.array([[[1,2,3],[4,5,6]]])
print(b)
print(b.ndim)

x = np.zeros(5,dtype="int")
print(x)

m = np.zeros([3,4])
print(m)

j = np.ones([5,5])
print(j)

f = np.full([3,3], 9)
print(f)

r = np.empty([2,4])
print(r)

id = np.identity(7, dtype="int")
print(id)

e = np.eye(6, k=2)
print(e)

num = np.arange(5,22,3)
print(num)