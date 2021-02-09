# quick sort


def quickSort(A, l, r):
    if(l >= r):
        return

    j = partition(A, l, r)
    quickSort(A, l, j-1)
    quickSort(A, j+1, r)


def partition(A, l, r):
    pivot = A[r]
    j = l
    for i in range(l, r):
        if A[i] <= pivot:
            A[i], A[j] = A[j], A[i]
            j = j + 1

    A[j], A[r] = A[r], A[j]
    return j


A = [29, 99, 27, 41, 66, 28, 44, 78, 87, 19,
     31, 76, 58, 88, 83, 97, 12, 21, 44, 0, 1]
quickSort(A, 0, len(A) - 1)
print(A)
