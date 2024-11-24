from random import randint
import random

# функция для сортировки вставками
def Insertion_Sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A

#функция для быстрой сортировки
def Quick_Sort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
    l_nums = [n for n in A if n < q]
    el_nums = [q] * A.count(q)
    r_nums = [n for n in A if n > q]
    return Quick_Sort(l_nums) + el_nums + Quick_Sort(r_nums)

# функция для сортировки выбором
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

#функция сортировки пузырьком
def Bubble_Sort(A):
    for i in range(len(arr)):
        flag = False
        for j in range(0, len(A) - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                flag = True
        if not flag:
            return A

#функция сортировки слиянием
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

#функция сортировки Шелла — последовательность Шелла
def Shell_Sort_Shell(A):
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

#функция сортировки Шелла — последовательность Хиббарда
def Shell_Sort_Hib(A):
    n = len(A)
    k = 0
    step = 1
    while step < n:
        step = 2 ** k - 1
        k += 1

    while step > 0:
        for i in range(step, n):
            value = A[i]
            j = i
            while j >= step and A[j - step] > value:
                A[j] = A[j - step]
                j -= step
            A[j] = value
        k -= 1
        step = 2 ** k - 1 if k > 0 else 0
    return A

#функция сортировки Шелла — последовательность Пратта
def generate_pratt(n):
    sequence = []
    i, j = 0, 0
    while True:
        value = (2 ** i) * (3 ** j)
        if value > n: break
        sequence.append(value)
        if i < j: j += 1
        else: i += 1
    return sequence

def Shell_Sort_Pratt(A):
    n = len(A)
    pratt_sequence = generate_pratt(n)
    pratt_sequence.reverse()
    for step in pratt_sequence:
        for i in range(step, n):
            value = A[i]
            j = i
            while j >= step and A[j - step] > value:
                A[j] = A[j - step]
                j -= step
            A[j] = value
    return A

#функции для пирамидальной сортировки
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


N = 100
#arr = [randint(1, 20000) for i in range(N)]
arr = [42, 7, 19, 86, 33, 58, 14, 91, 27, 65, 3, 74, 12, 50, 88, 88, 88]
#arr = [5, 2, 4, 7, 1, 3, 2, 6]
arr_sort = arr.copy()
arr_sort.sort()
print(arr)
arr = Quick_Sort(arr)
print(arr_sort)
#print(Insertion_Sort(arr))
print(arr)
#print(Selection_Sort(arr))
#print(shuffle(arr))
#print(Bubble_Sort(arr))
#print(Merge_Sort(arr, 0, len(arr) - 1))
#print(Shell_Sort(arr))
#print(Heap_Sort(arr))
print(arr==arr_sort)
