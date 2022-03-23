import numpy as np

np.random.seed(10)
a = np.random.rand(2, 3)
b = np.random.randn(3, 2)
c = np.random.rand(6)
d = np.random.randint(1, 100, 6)
c = np.reshape(c, (2, 3))
d = d.reshape(2, -1)

print('a shape: ', a.shape, '\n', a)
print('b shape: ', b.shape, '\n', b)
print('c shape: ', c.shape, '\n', c)
print('d shape: ', d.shape, '\n', d)

print('다차원 객체 1차원 변환 방법')
print('a = ', a.flatten())
print('b = ', np.ravel(b))
print('c = ', np.reshape(c, (-1)))
print('d = ', d.reshape(-1, ))
