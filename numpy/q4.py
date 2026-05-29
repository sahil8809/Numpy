import numpy as np
marks = np.array([85, 90, 78, 92, 60])
print("Marks:", marks)
passed = marks[marks >= 70]
print("Passed Students:", passed)
print("First 3 Marks:", marks[:3])
# print("Last Mark:", marks[-1])
print("Total:", np.sum(marks))
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))