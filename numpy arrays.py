import numpy as np

a=np.array([[1,2,5,3],[6,8,8,5]])
print(a)
print(type(a))
print(a.size)
print(a.ndim)
print(a.shape)


a0=np.array([[1,2,3],[4,5,6]])
c=a0.reshape(3,2)
# print(a0)
# print(c)

a1=np.zeros([3,5])
# print(a1)

a2=np.arange(25)
# print(a2)

a3=np.full((3,5),6)
# print(a3)

a4=np.eye(4)
# print(a4)

r=np.random.random((4,5))
# print(r)

s=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(s[-1,-4:-1])

# Both new and dub point the array [1,2,3], so change in one reflects in another
new=np.array([1,2,3])
dub=new
dub[0]=40
# print(new[0])

# For no change:
new=np.array([1,2,3,4])
dub=new.copy()
dub[0]=43
# print(dub[0])
# print(new[0])

a=np.array([1,2,3])
b=np.array([4,5,6])

# print(np.add(a,b)) #a+b
# print(np.subtract(a,b)) #a-b
# print(np.multiply(a,b)) #a*b
# print(np.divide(a,b)) #a/b
# print(np.sqrt(a)) #sqrt of a


d=np.array([[1,2,3,4],[5,6,7,8]])
# print(d)
# print(d.T)


a=np.array([[1,2,3],[4,5,6]])
print(a)
print(np.sum(a))
print(np.sum(a,axis=0))
print(np.sum(a,axis=1))
