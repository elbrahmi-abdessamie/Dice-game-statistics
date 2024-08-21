import numpy as np
import matplotlib.pyplot as plt

def visual_plot(active: bool=True, v: str='all'):

    def plotter(function):
        def wrapper(*args):
            to_plot = function(*args)
            if active:
                plt.plot(to_plot)
                plt.yticks(range(0, 110, 10))
                if v == 'one':
                    plt.show()
                    plt.clf()
            return to_plot
        return wrapper
    return plotter

@visual_plot(active=False)
def random_roll(num: int = 100, start: int = 0)-> list[int]:
    result = [start]
    x = 0
    while x < num:
        step = result[-1]
        dice = np.random.randint(1,7)
        
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        clumsy_event = np.random.rand()
        if clumsy_event <= 0.005:
            step = max(0, step -6)
        result.append(max(step, 0))
        x += 1
    return result

def distribution_plot(function):
    def wrapper(*args):
        np_all_w = np.array(function(*args))
        plt.hist(np_all_w[:, -1])
        plt.show()
    return wrapper

@distribution_plot
def simulator(sim_times: int=500):
    all_random_walks = []
    for i in range(sim_times):
        np.random.seed(i+666)
        all_random_walks.append(random_roll())
    return all_random_walks
    

def main():
    simulator()

if __name__ == '__main__':
    main()