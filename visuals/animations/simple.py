import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()


def animate(frame):
    global ax
    ax.cla()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    # ax.plot(frame, frame)
    line, = ax.plot(frame, frame, 'ro')
    return line



def run():
    global fig
    some_animation = animation.FuncAnimation(fig, animate, frames=10, interval=1000)
    plt.show()



run()