import sys
import matplotlib.pyplot as plt

from plot import *



if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    input_sizes = [10, 50, 100, 500, 1000, 5000, 10000]
    qs_y = []
    qs_y_maxes = []
    ms_y = []
    ms_y_maxes = []
    for i in input_sizes:
        (qs0, ms0) = get_stats(run_randqs, run_ms, i)
        qs_y.append(qs0[0])
        ms_y.append(ms0[0])
        qs_y_maxes.append(qs0[1])
        ms_y_maxes.append(ms0[1])
    
    print_results(input_sizes, qs_y, qs_y_maxes, input_sizes, ms_y, ms_y_maxes, name1="rand QS", name2="MS")
    get_graph(input_sizes, qs_y, qs_y_maxes, input_sizes, ms_y, ms_y_maxes, name1="rand QS", name2="MS")






