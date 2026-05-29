import numpy as np
a = np.array([10, 20, 30, 40, 50])
print("Original Array :", a)
print("First Element :", a[0])

print("Last Element :", a[-1])
print("Slicing :", a[1:4])

print("Multiply by 2 :", a * 2)

print("Addition :", a + 5)

print("Sum :", a.sum())
print("Maximum :", a.max())

print("Minimum :", a.min())
print("Mean :", a.mean())
print("Datatype :", a.dtype)
print("Shape :", a.shape)

b = np.array([[1, 2], [3, 4]])
print("2D Array :\n", b)
print("Shape of 2D Array :", b.shape)
print("Zeros Array :\n", np.zeros((2, 3)))
print("Ones Array :\n", np.ones((2, 2)))
print("Random Numbers :", np.random.randint(1, 10, 5))
print("Arange :", np.arange(1, 11))