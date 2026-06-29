import matplotlib.pyplot as plt
import numpy as np

# Generate some random data for demonstration
data1 = np.random.randn(1000)
data2 = np.random.randn(1000)
data3 = np.random.randn(1000)
data4 = np.random.randn(1000)

plt.figure(figsize=(10, 8)) # Optional: set the overall figure size

# First subplot (top-left)
plt.subplot(2, 2, 1)
plt.hist(data1, bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram 1 (2,2,1)')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Second subplot (top-right)
plt.subplot(2, 2, 2)
plt.hist(data2, bins=30, color='salmon', edgecolor='black')
plt.title('Histogram 2 (2,2,2)')
plt.xlabel('Value')

# Third subplot (bottom-left)
plt.subplot(2, 2, 3)
plt.hist(data3, bins=30, color='lightgreen', edgecolor='black')
plt.title('Histogram 3 (2,2,3)')
plt.xlabel('Value')

# Fourth subplot (bottom-right)
plt.subplot(2, 2, 4)
plt.hist(data4, bins=30, color='gold', edgecolor='black')
plt.title('Histogram 4 (2,2,4)')
plt.xlabel('Value')

plt.tight_layout() # Adjust layout to prevent overlapping titles/labels
plt.show()