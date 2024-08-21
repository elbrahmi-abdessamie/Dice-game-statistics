import numpy as np
import matplotlib.pyplot as plt

def visual_plot(active: bool=True):

    def plotter(function):
        def wrapper(*args):
            to_plot = function(*args)
            if active:
                plt.plot(to_plot)
                plt.yticks(range(0, 110, 10))
            return to_plot
        return wrapper
    return plotter

@visual_plot(active=True)
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

def simulator(sim_times: int=500):
    all_random_walks = []
    for i in range(sim_times):
        np.random.seed(i+666)
        all_random_walks.append(random_roll())
    plt.show()
    np_all_w = np.array(all_random_walks)[:,-1]
    plt.hist(np_all_w, color='lightgreen', ec='black')
    plt.show()
    # return np.array([row[-1] for row in all_random_walks])
    return np_all_w
    
def odds_calculater(value: int, ends: np.ndarray, sim_count: int = 500):
    count = np.count_nonzero(ends >= value)
    est_chance = count / 500 * 100
    print(f"the estimated chance that you'll reach at least {value} steps\
 high if you play this Empire State Building game is {est_chance:.2f}%")
    

def main():
    ends = simulator()
    odds_calculater(80, ends)


if __name__ == '__main__':
    main()