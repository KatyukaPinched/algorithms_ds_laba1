from time import *
import numpy as np
import matplotlib.pyplot as plt
import random
from random import randint
from math import *

def Insertion_Sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A

def Selection_Sort(A):
    index = 0
    index_min = 0 

    for i in range(index_min, len(A) - 1): 
        for j in range(i + 1, len(A)):
            if A[j] < A[index_min]:
                index_min = j
        A[index], A[index_min] = A[index_min], A[index]
        index += 1
        index_min = index
    return A

def Bubble_Sort(A):

    for i in range(len(arr)):
        flag = False
        for j in range(0, len(A) - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                flag = True
        if not flag:
            return A

def Merge_Sort(A, p, r):
    if p < r:
        q = int((p + r)/2)
        Merge_Sort(A, p, q)
        Merge_Sort(A, q + 1, r)
        Merge(A, p, q, r)
    return A

def Merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    for i in range(n1):
        L.append(A[p + i])
    for j in range(n2):
        R.append(A[q + j + 1])
    L.append(float('inf'))
    R.append(float('inf'))
    i = j = 0

    for k in range(p, r + 1):
        if(L[i] <= R[j]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A

def Shell_Sort(A):
    step = len(A)//2

    while step > 0:
        for i in range(step, len(A)):
            value = A[i]
            while i >= step and A[i - step] > value:
                A[i] = A[i - step]
                i -= step
                A[i] = value
        step //= 2
    return A

def Quick_Sort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
    l_nums = [n for n in A if n < q]

    el_nums = [q] * A.count(q)
    r_nums = [n for n in A if n > q]
    return Quick_Sort(l_nums) + el_nums + Quick_Sort(r_nums)

def Parent(i): return (i - 1) // 2
def Left(i): return 2 * i + 1
def Right(i): return 2 * i + 2

def Max_Heapify(A, i, heap_size):
    l = Left(i)
    r = Right(i)
    largest = i
    if l < heap_size and A[l] > A[largest]:
        largest = l
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        Max_Heapify(A, largest, heap_size)

def Build_Max_Heap(A):
    heap_size = len(A)
    for i in range(heap_size // 2 - 1, -1, -1):
        Max_Heapify(A, i, heap_size)

def Heap_Sort(A):
    Build_Max_Heap(A)
    heap_size = len(A)

    for i in range(heap_size - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        Max_Heapify(A, 0, i)
    return A

time_arr_Insertion = []
time_arr_Selection = []
time_arr_Bubble = []
time_arr_Merge = []
time_arr_Shell = []
time_arr_Quick = []
time_arr_Heap = []
x_arr_Insertion = []
x_arr_Selection = []
x_arr_Bubble = []
x_arr_Merge = []
x_arr_Shell = []
x_arr_Quick = []
x_arr_Heap = []

for i in range(0, 2000, 100):

    arr = [randint(1, 1000) for _ in range(i)]
    save_arr_Invertion = arr
    save_arr_Selection = arr
    save_arr_Bubble = arr
    save_arr_Merge = arr
    save_arr_Shell = arr
    save_arr_Quick = arr
    save_arr_Heap = arr

    start_time = time()
    Insertion_Sort(save_arr_Invertion)
    finish_time = time()
    time_arr_Insertion.append(finish_time-start_time)
    x_arr_Insertion.append(i)

    start_time = time()
    Selection_Sort(save_arr_Selection)
    finish_time = time()
    time_arr_Selection.append(finish_time-start_time)
    x_arr_Selection.append(i)
    
    start_time = time()
    Bubble_Sort(save_arr_Bubble)
    finish_time = time()
    time_arr_Bubble.append(finish_time-start_time)
    x_arr_Bubble.append(i)

    start_time = time()
    Merge_Sort(save_arr_Merge, 0, len(save_arr_Merge)-1)
    finish_time = time()
    time_arr_Merge.append(finish_time-start_time)
    x_arr_Merge.append(i)

    start_time = time()
    Shell_Sort(save_arr_Shell)
    finish_time = time()
    time_arr_Shell.append(finish_time-start_time)
    x_arr_Shell.append(i)

    start_time = time()
    Quick_Sort(save_arr_Quick)
    finish_time = time()
    time_arr_Quick.append(finish_time-start_time)
    x_arr_Quick.append(i)

    start_time = time()
    Heap_Sort(save_arr_Bubble)
    finish_time = time()
    time_arr_Heap.append(finish_time-start_time)
    x_arr_Heap.append(i)


p_Insertion = np.polyfit(x_arr_Insertion, time_arr_Insertion, 2)
p_Selection = np.polyfit(x_arr_Selection, time_arr_Selection, 2)
p_Bubble = np.polyfit(x_arr_Bubble, time_arr_Bubble, 2)
p_Merge = np.polyfit(x_arr_Merge, time_arr_Merge, 2)
p_Shell = np.polyfit(x_arr_Shell, time_arr_Shell, 2)
p_Quick = np.polyfit(x_arr_Quick, time_arr_Quick, 2)
p_Heap = np.polyfit(x_arr_Heap, time_arr_Heap, 2)

plt.figure(figsize=(10, 6))
plt.scatter(x_arr_Insertion,time_arr_Insertion)
plt.scatter(x_arr_Selection,time_arr_Selection)
plt.scatter(x_arr_Bubble,time_arr_Bubble)
plt.scatter(x_arr_Merge,time_arr_Merge)
plt.scatter(x_arr_Shell,time_arr_Shell)
plt.scatter(x_arr_Quick,time_arr_Quick)
plt.scatter(x_arr_Heap,time_arr_Heap)

plt.xlabel('n — номер элемента массива')
plt.ylabel('t — время работы программы')
plt.legend()
plt.grid()

plt.plot(x_arr_Insertion, np.polyval(p_Insertion, x_arr_Insertion), label='Сортировка вставками', color='red')
plt.plot(x_arr_Selection, np.polyval(p_Selection, x_arr_Selection), label='Сортировка выбором', color='blue')
plt.plot(x_arr_Bubble, np.polyval(p_Bubble, x_arr_Bubble), label='Сортировка пузырьком', color='green')
plt.plot(x_arr_Merge, np.polyval(p_Merge, x_arr_Merge), label='Сортировка слиянием', color='red')
plt.plot(x_arr_Shell, np.polyval(p_Shell, x_arr_Shell), label='Сортировка Шелла', color='blue')
plt.plot(x_arr_Quick, np.polyval(p_Quick, x_arr_Quick), label='Быстрая сортировка', color='green')
plt.plot(x_arr_Heap, np.polyval(p_Heap, x_arr_Heap), label='Пирамидальная сортировка', color='pink')

plt.tight_layout()
plt.legend()
plt.show()