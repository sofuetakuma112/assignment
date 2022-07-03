import numpy as np
import matplotlib.pyplot as plt

axes = [plt.subplots() for _ in range(2)]

axes[0][1].hist(np.random.rand(10000), bins=50)

axes[1][1].hist(np.random.randn(10000), bins=50)

xs = np.arange(0, 5.1, 0.1)
xs_deg = np.arange(0, 360, 1)
fig = plt.figure()
for i in range(3):
  figNum = i + 1
  ax = fig.add_subplot(230 + figNum)
  ax.plot(xs, list(map(lambda x: x ** figNum, xs)))
  
ax = fig.add_subplot(234)
ax.plot(xs_deg, list(map(lambda x: np.sin(x * np.pi / 180), xs_deg)))
ax.set_ylim(-1, 1)

ax = fig.add_subplot(235)
ax.plot(xs_deg, list(map(lambda x: np.cos(x * np.pi / 180), xs_deg)))
ax.set_ylim(-1, 1)

ax = fig.add_subplot(236)
ax.plot(np.arange(-90, 91, 1), list(map(lambda x: np.tan(x * np.pi / 180), np.arange(-90, 91, 1))))
ax.set_xlim(-90, 90)
ax.set_ylim(-1, 1)

plt.show()