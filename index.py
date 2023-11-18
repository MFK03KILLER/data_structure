import matplotlib.pyplot as plt
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    return sorted_arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

dataset = [1000, 5000, 20000, 1500, 30000]  # Replace with your own dataset

bubble_sort_time = []
selection_sort_time = []
counting_sort_time = []
quick_sort_time = []

for i in range(1, len(dataset) + 1):
    subset = dataset[:i]
    
    start_time = time.time()
    bubble_sort(subset)
    bubble_sort_time.append(time.time() - start_time)
    
    start_time = time.time()
    selection_sort(subset)
    selection_sort_time.append(time.time() - start_time)
    
    start_time = time.time()
    counting_sort(subset)
    counting_sort_time.append(time.time() - start_time)
    
    start_time = time.time()
    quick_sort(subset)
    quick_sort_time.append(time.time() - start_time)

plt.plot(range(1, len(dataset) + 1), bubble_sort_time, label='Bubble Sort')
plt.plot(range(1, len(dataset) + 1), selection_sort_time, label='Selection Sort')
plt.plot(range(1, len(dataset) + 1), counting_sort_time, label='Counting Sort')
plt.plot(range(1, len(dataset) + 1), quick_sort_time, label='Quicksort')

plt.xlabel('Andaze Data vorodi')
plt.ylabel('Zaman(bar hasb sanie)')
plt.title('Moghayese sorat amalkard algoithm ha')
plt.legend()

plt.show()
