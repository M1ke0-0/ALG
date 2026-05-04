import random

class Stats:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0
        self.partitions = 0
        self.max_depth = 0
        self.logs = []  # первые 3 разбиения


# ---------------- PIVOT ----------------
def choose_pivot(arr, left, right, mode):
    if mode == "first":
        return left
    elif mode == "middle":
        return (left + right) // 2
    elif mode == "random":
        return random.randint(left, right)


# ---------------- ЛОМУТО ----------------
def partition_lomuto(arr, left, right, stats, depth, pivot_mode):
    stats.partitions += 1

    pivot_index = choose_pivot(arr, left, right, pivot_mode)
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    stats.swaps += 1

    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        stats.comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            stats.swaps += 1

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    stats.swaps += 1

    if len(stats.logs) < 3:
        stats.logs.append((left, right, pivot, arr.copy(), i + 1))

    return i + 1


def quicksort_lomuto(arr, left, right, stats, depth=1, pivot_mode="first"):
    stats.max_depth = max(stats.max_depth, depth)

    if left < right:
        p = partition_lomuto(arr, left, right, stats, depth, pivot_mode)
        quicksort_lomuto(arr, left, p - 1, stats, depth + 1, pivot_mode)
        quicksort_lomuto(arr, p + 1, right, stats, depth + 1, pivot_mode)


# ---------------- ХОАР ----------------
def partition_hoare(arr, left, right, stats, depth, pivot_mode):
    stats.partitions += 1

    pivot_index = choose_pivot(arr, left, right, pivot_mode)
    pivot = arr[pivot_index]

    i = left - 1
    j = right + 1

    while True:
        while True:
            i += 1
            stats.comparisons += 1
            if arr[i] >= pivot:
                break

        while True:
            j -= 1
            stats.comparisons += 1
            if arr[j] <= pivot:
                break

        if i >= j:
            if len(stats.logs) < 3:
                stats.logs.append((left, right, pivot, arr.copy(), j))
            return j

        arr[i], arr[j] = arr[j], arr[i]
        stats.swaps += 1


def quicksort_hoare(arr, left, right, stats, depth=1, pivot_mode="first"):
    stats.max_depth = max(stats.max_depth, depth)

    if left < right:
        p = partition_hoare(arr, left, right, stats, depth, pivot_mode)
        quicksort_hoare(arr, left, p, stats, depth + 1, pivot_mode)
        quicksort_hoare(arr, p + 1, right, stats, depth + 1, pivot_mode)


# ---------------- ДАННЫЕ ----------------
orders_random = [57,14,83,29,61,45,72,10,34,98,21,66,39,50,7,66,28,64,72,62,66,26,8,29,89,35,15,32,27,55,3,59,100,21,56,85,36,23,75,18,49,18,78,44,59,59,96,68,23,81,89,4,25,90,92,72,8,82,89,44,82,55,49,23,49,80,22,84,67,21,88,65,73,99,88,49,92,39,83,66,83,26,53,75,56,94,59,89,71,37,64,99,96,73,83,30,79,78,29,7]

orders_many_duplicates = [5,3,5,2,5,1,5,4,5,0,5,3,5,2,5,1,9,7,0,10,4,8,2,6,3,10,5,1,9,0,4,7,2,8,3,6,10,5,1,9,4,0,7,2,8,6,3,10,5,1,9,0,4,7,8,2,6,3,10,5,1,9,0,4,7,2,8,6,3,10,5,1,9,0,4,7,2,8,6,3,10,5,1,9,0,4,7,2,8,6,3,10,5,1,9,0,4,7,2,8]


# ---------------- ЗАПУСК ----------------
def run_test(arr, scheme, pivot_mode):
    a = arr.copy()
    stats = Stats()

    if scheme == "lomuto":
        quicksort_lomuto(a, 0, len(a) - 1, stats, pivot_mode=pivot_mode)
    else:
        quicksort_hoare(a, 0, len(a) - 1, stats, pivot_mode=pivot_mode)

    print(f"\nСхема: {scheme}, pivot: {pivot_mode}")
    print("Отсортированный:", a)
    print(f"Сравнения: {stats.comparisons}, Обмены: {stats.swaps}")
    print(f"Разбиения: {stats.partitions}, Глубина: {stats.max_depth}")

    print("\nПервые 3 разбиения:")
    for log in stats.logs:
        l, r, pivot, state, ret = log
        print(f"[{l}:{r}] pivot={pivot} → индекс={ret}")
        print(state)


def run():
    for data_name, data in {
        "Случайный": orders_random,
        "Много дубликатов": orders_many_duplicates
    }.items():

        print(f"\n\n===== {data_name} массив =====")

        for scheme in ["lomuto", "hoare"]:
            for pivot in ["first", "middle", "random"]:
                run_test(data, scheme, pivot)


run()