import time
import random


def bubble_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        for i in range(n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
def selectionSort(array, size):
    for ind in range(size):
        max_index = ind
        for j in range(ind + 1, size):
            if array[j] > array[max_index]:
                max_index = j
        array[ind], array[max_index] = array[max_index], array[ind]
        
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]
    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] >= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] > pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
        
        
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

print("Agora com um array de 6")

array_size = 6
random_array = [random.randint(0, 1000) for _ in range(array_size)]


for sort_name, sort_function in [
    ("Quick Sort", lambda arr: quickSort(arr, 0, len(arr) - 1)),
    ("Merge Sort", lambda arr: mergeSort(arr, 0, len(arr) - 1)),
    ("Selection Sort", lambda arr: selectionSort(arr, len(arr))),
    ("Insertion Sort", insertionSort),
    ("Bubble Sort", bubble_sort)
]:
    arr_copy = random_array.copy()
    execution_time = measure_time(sort_function, arr_copy)
    print(f"{sort_name} execution time: {execution_time:.6f} seconds")
    
print("Agora com um array de 12")

array_size_2 = 12
random_array_2 = [random.randint(0, 1000) for _ in range(array_size_2)]


for sort_name, sort_function in [
    ("Quick Sort", lambda arr: quickSort(arr, 0, len(arr) - 1)),
    ("Merge Sort", lambda arr: mergeSort(arr, 0, len(arr) - 1)),
    ("Selection Sort", lambda arr: selectionSort(arr, len(arr))),
    ("Insertion Sort", insertionSort),
    ("Bubble Sort", bubble_sort)
]:
    arr_copy = random_array_2.copy()
    execution_time = measure_time(sort_function, arr_copy)
    print(f"{sort_name} execution time: {execution_time:.6f} seconds")