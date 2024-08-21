import numpy as np
import matplotlib.pyplot as plt

def plotter(function):
    def wrapper(*args):
        to_plot = function(*args)
        plt.plot(to_plot)
        plt.show()
        plt.cla()
    return wrapper

@plotter
def random_roll(num: int, start: int)-> list[int]:
    result = [start]
    for x in range(num) :
        step = result[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        result.append(max(step, 0))
    return result

random_roll(100, 0)
random_roll(100, 0)
