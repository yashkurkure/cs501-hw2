import random


def quicksort(array):
    _quicksort(array, 0, len(array) - 1)

def _quicksort(array, lo , hi):
    if(lo < hi):
        pivot = getpivot(array, lo, hi)
        _quicksort(array , lo , pivot-1)
        _quicksort(array, pivot + 1, hi)
  
def getpivot(array , lo, hi):
    pivot = random.randrange(lo, hi)
    array[lo], array[pivot] = array[pivot], array[lo]
    return partition(array, lo, hi)
  
def partition(array, lo, hi):
    pivot = lo
    i = lo + 1 

    for j in range(lo + 1, hi + 1):
        if array[j] <= array[pivot]:
            array[i] , array[j] = array[j] , array[i]
            i = i + 1
    array[pivot] , array[i - 1] = array[i - 1] , array[pivot]
    pivot = i - 1
    return (pivot)

if __name__ == "__main__":
    array = [2, 10, 4, 33, 23, 0]
    quicksort(array)
    print(array)