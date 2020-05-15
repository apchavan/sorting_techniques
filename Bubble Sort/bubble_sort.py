# Bubble sort algorithm using NumPy array

import numpy as np


def bubble_sort(arr: np.ndarray):
    total_len: int = len(arr)
    n_passes: int = 0
    for i in range(0, total_len):
        for j in range(0, (total_len - i - 1)):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        n_passes += 1
    return arr, n_passes


arr: np.ndarray = np.array([1, 2, 3], dtype=np.int)
print(f"\n(*) Input = {arr} ; Total elements => {len(arr)}")
print("(*) Sorted array = %s ; Total pass => %s" % (bubble_sort(arr=arr.copy())))

arr: np.ndarray = np.array([5, 4, -2, -1], dtype=np.int)
print(f"\n(*) Input = {arr} ; Total elements => {len(arr)}")
print("(*) Sorted array = %s ; Total pass => %s" % (bubble_sort(arr=arr.copy())))

arr: np.ndarray = np.array([5, 4, 3, 2, 1], dtype=np.int)
print(f"\n(*) Input = {arr} ; Total elements => {len(arr)}")
print("(*) Sorted array = %s ; Total pass => %s" % (bubble_sort(arr=arr.copy())))
