# Selection sort algorithm using NumPy array

import numpy as np


def selection_sort(arr: np.ndarray):
    total_len: int = len(arr)
    for i in range(total_len):
        m_index: int = i
        for j in range((i + 1), total_len):
            if arr[m_index] > arr[j]:
                m_index = j
        if m_index != i:
            arr[i], arr[m_index] = arr[m_index], arr[i]
        print(f"\ti={i}, m_index={m_index}, arr={arr}")
    return arr


arr: np.ndarray = np.array([4, 3, 3, -1, 1], dtype=np.int)
print(f"\n(*) Input = {arr} ; Total elements => {len(arr)}")
print("(*) Sorted array = %s" % (selection_sort(arr=arr.copy())))
