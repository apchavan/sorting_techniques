# Insertion sort algorithm using NumPy array

import numpy as np


def insertion_sort(arr: np.ndarray):
    total_len: int = len(arr)

    for i in range(1, total_len):
        key: int = arr[i]
        j: int = (i - 1)
        # print(f"\ni={i}, before={arr}")       # <- First print statement
        while (j >= 0) and (key < arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        # print(f"    shifted={arr}")           # <- Second print statement
        arr[j + 1] = key
        # print(f"   assigned={arr}")           # <- Third print statement
    return arr


arr: np.ndarray = np.array([4, 3, 3, -1, 1], dtype=np.int)
print(f"\n INPUT = {arr} ; Total elements => {len(arr)}")
print("\n(*) Sorted array = %s" % (insertion_sort(arr=arr.copy())))
