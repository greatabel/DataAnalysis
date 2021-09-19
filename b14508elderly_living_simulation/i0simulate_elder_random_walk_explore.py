import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# setting up steps for simulating 2D
dims = 2
step_n = 30
step_set = [-1, 0, 1]
origin = np.zeros((1, dims))

# Simulate steps in 2D
step_shape = (step_n, dims)
steps = np.random.choice(a=step_set, size=step_shape)
path = np.concatenate([origin, steps]).cumsum(0)
start = path[:1]
stop = path[-1:]

# plot the figure
fig, ax = plt.subplots()
(line,) = ax.plot([], [], lw=4, c="orange", ls="dotted")
xdata, ydata = [], []


# This function returns a tuple containing elements of random walk path
def data_extract():
    for pos in range(len(path)):
        sample = path[pos]
        yield sample[0], sample[1]


def init():
    ax.set_ylim(-10, 10)
    ax.set_xlim(-5, 10)
    ax.plot(start[:, 0], start[:, 1], c="red", marker="*")
    ax.plot(stop[:, 0], stop[:, 1], c="black", marker="o")
    plt.title("Elderly Random Walk Without Furniture")
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)

    return (line,)


def animate(data):
    # get data from path using function and
    t, y = data

    xdata.append(t)
    ydata.append(y)
    line.set_data(xdata, ydata)
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()

    # below code of if statements are to re-size the simulation if the random walk goes out of the frame
    if t >= xmax:
        ax.set_xlim(2 * xmin, 2 * xmax)
        ax.figure.canvas.draw()

    if t < xmin:
        ax.set_xlim(2 * xmin, 2 * xmax)
        ax.figure.canvas.draw()

    if y <= ymin:
        ax.set_ylim(2 * ymin, 2 * ymax)
        ax.figure.canvas.draw()

    if t >= ymax:
        ax.set_ylim(2 * ymin, 2 * ymax)
        ax.figure.canvas.draw()

    line.set_data(xdata, ydata)

    return (line,)


anim = animation.FuncAnimation(
    fig, animate, data_extract, blit=False, init_func=init, interval=10, repeat=False
)

plt.show()
