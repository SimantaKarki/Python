# selection sort bubblesort and insertion sort


def selectionSort(A):
    for i in range(0, len(A)):
        min = i
        for j in range(i+1, len(A)):
            if A[min] > A[j]:
                min = j
        A[i], A[min] = A[min], A[i]

    print("The sorted array using selection sort is:")
    print(A)


def bubbleSort(A):
    for k in range(len(A)-1):
        for i in range(0, len(A)-k-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]

    print("The sorted array using Bubblesort is:")
    print(A)


def insertionSort(A):
    for i in range(1, len(A)):
        value = A[i]
        hole = i
        while(hole > 0 and A[hole-1] > value):
            A[hole] = A[hole-1]
            hole = hole - 1
        A[hole] = value
    print("The sorted list using insertion sort is:\n", A)


if __name__ == "__main__":
    A = [234, 56, 78, 45, 90, 1, 3, 57, 76, 4, 0]
    # selectionSort(A)
    # bubbleSort(A)
    insertionSort(A)
