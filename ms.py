def mergesort(array):
    _mergesort(array, 0, len(array) - 1)

def _mergesort(array, lo, hi):
    if lo < hi:
        mid = lo+(hi-lo)//2
        _mergesort(array, lo, mid)
        _mergesort(array, mid+1, hi)
        merge(array, lo, mid, hi)

def merge(array, lo, mid, hi):
    left_size = mid - lo + 1
    right_size = hi - mid
    left = [0] * (left_size)
    right = [0] * (right_size)
 

    for i in range(0, left_size):
        left[i] = array[lo + i]
 
    for j in range(0, right_size):
        right[j] = array[mid + 1 + j]

    i = 0 
    j = 0 
    k = lo
 
    while i < left_size and j < right_size:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
 
    while i < left_size:
        array[k] = left[i]
        i += 1
        k += 1
 
    while j < right_size:
        array[k] = right[j]
        j += 1
        k += 1

if __name__ == "__main__":
    array = [2, 10, 4, 33, 23, 0]
    mergesort(array)
    print(array)