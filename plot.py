import time
import copy
from input_gen import gen_random_list
from rand_qs import quicksort
from ms import mergesort
import matplotlib.pyplot as plt

def print_results(
    sort1_x1, 
    sort1_y1, 
    sort1_y1_maxes,
    sort2_x2, 
    sort2_y2,
    sort2_y2_maxes,
    name1 = "sort1", 
    name2 = "sort2"):
    
    print ("input size" + "," + name1 + " time" + "," + name1 + " maxtime" + "," + name2 + " time" + "," + name2 + " maxtime")
    for i in range(0, len(sort1_x1)):
        print(str(sort1_x1[i]) + "," + str(sort1_y1[i]) + "," + str(sort1_y1_maxes[i]) + "," + str(sort2_y2[i]) + "," + str(sort2_y2_maxes[i]))

def get_graph(
    sort1_x1, 
    sort1_y1, 
    sort1_y1_maxes,
    sort2_x2, 
    sort2_y2,
    sort2_y2_maxes,
    name1 = "sort1", 
    name2 = "sort2"):

    plt.plot(sort1_x1, sort1_y1, label = name1)

    plt.scatter(sort1_x1, sort1_y1_maxes, label = name1 + " max time")

    plt.plot(sort2_x2, sort2_y2, label = name2)

    plt.scatter(sort2_x2, sort2_y2_maxes, label = name2 + " max time")

    ax = plt.gca()

    # Set x logaritmic
    ax.set_xscale('log')

    plt.xlabel('input size')

    plt.ylabel('runtime')

    plt.title('runtime vs input-size')

    plt.legend()
    plt.show()

def get_stats(sort1, sort2, size, iterations=30):

    input = gen_random_list(size)

    avg_time_sort1 = 0.0
    max_time_sort1 = 0.0

    avg_time_sort2 = 0.0
    max_time_sort2 = 0.0

    # run the input on sort1 iteration times
    for i in range(0, iterations):
        array = copy.deepcopy(input)
        time_taken = sort1(array)
        if max_time_sort1 < time_taken:
            max_time_sort1 = time_taken
        avg_time_sort1 = avg_time_sort1 + time_taken
    avg_time_sort1 = avg_time_sort1/iterations

    # run the input on sort2 iteration times
    for i in range(0, iterations):
        array = copy.deepcopy(input)
        time_taken = sort2(array)
        if max_time_sort2 < time_taken:
            max_time_sort2 = time_taken
        avg_time_sort2 = avg_time_sort2 + time_taken
    avg_time_sort2 = avg_time_sort2/iterations

    return ( (avg_time_sort1, max_time_sort1), (avg_time_sort2, max_time_sort2))


def run_randqs(input):
    start = time.time()
    quicksort(input)
    end = time.time()
    return end-start

def run_ms(input):
    start = time.time()
    mergesort(input)
    end = time.time()
    return end-start