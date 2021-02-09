# merge sort using recursion
def mergeSort(A, l, r):
    if (l >= r):
        return
    mid = (l+r)//2
    mergeSort(A, l, mid)
    mergeSort(A, mid+1, r)
    merge(A, l, mid, r)


def merge(A, l, m, r):
    first_half = A[l:m+1]
    second_half = A[m+1:r+1]
    i = 0
    j = 0
    k = l

    while i < len(first_half) and j < len(second_half):
        if first_half[i] <= second_half[j]:
            A[k] = first_half[i]
            i += 1
        else:
            A[k] = second_half[j]
            j += 1
        k = k+1

    while i < len(first_half):
        A[k] = first_half[i]
        i = i + 1
        k = k + 1

    while j < len(second_half):
        A[k] = second_half[j]
        j = j + 1
        k = k + 1


if __name__ == "__main__":
    A = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 0, 26]
    mergeSort(A, 0, len(A)-1)
    print(A)
