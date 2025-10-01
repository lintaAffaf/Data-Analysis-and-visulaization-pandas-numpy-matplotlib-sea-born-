import numpy as np
my_List=[1,2,3]

arr=np.zeros(10)
print(arr)

nice=np.ones(10)
print(nice)

fives=np.ones(10)*5
print(fives)

grr=np.arange(10,51,2)
print(grr)

matrix=np.arange(9).reshape(3,3)
print(matrix)

identity_matrix=np.eye(3)
print(identity_matrix)

random=np.random.randn(25)
print(random)

desig=np.arange(1,101).reshape(10,10)/100
print(desig)

print(np.linspace(0,1,20))
