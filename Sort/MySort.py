def selection_sort(a):
    for i in range(0, len(a) - 1):
        minimum = i
        for j in range(i, len(a)):
            if a[minimum] > a[j]:
                minimum = j
        a[i], a[minimum] = a[minimum], a[i]


# 거의 정렬된 상태에서 가장 우수한 성능
def insertion_sort(a):
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j - 1] > a[j]:
                a[j], a[j - 1] = a[j - 1], a[j]


# 입력 크기가 작은경우 좋음 특히 임베디드시스템에서 많이 사용함
def shell_sort(a):
    h = 4
    while h >= 1:
        for i in range(h, len(a)):
            j = i
            while j >= h and a[j] < a[j - h]:
                a[j], a[j - h] = a[j - h], a[j]
                j -= h
        h //= 3


def merge_sort(a, b, low, high):
    if high <= low:
        return
    mid = low + (high - low) // 2
    merge_sort(a, b, low, mid)
    merge_sort(a, b, mid + 1, high)
    merge(a, b, low, mid, high)


def merge(a, b, low, mid, high):
    i = low
    j = mid + 1
    for k in range(low, high + 1):
        if i > mid:
            b[k] = a[j]
            j += 1
        elif j > high:
            b[k] = a[i]
            i += 1
        elif a[j] < a[i]:
            b[k] = a[j]
            j += 1
        else:
            b[k] = a[i]
            i += 1
    for k in range(low, high + 1):
        a[k] = b[k]


def quick_sort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        quick_sort(a, low, pivot - 1)
        quick_sort(a, pivot + 1, high)


def partition(a, pivot, high):
    i = pivot + 1
    j = high
    while True:
        while i < high and a[i] < a[pivot]:
            i += 1
        while j > pivot and a[j] > a[pivot]:
            j -= 1
        if j <= i:
            break
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    a[pivot], a[j] = a[j], a[pivot]
    return j


if __name__ == '__main__':
    a = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
    print("정렬 전:\t", end="")
    print(a)
    selection_sort(a)
    print("정렬 후:\t", end="")
    print(a)
