def merge(left, right):
    merged = []
    i = j = 0
    comparisons = 0

    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, comparisons


# 🔹 РЕКУРСИВНАЯ ВЕРСИЯ
def merge_sort_recursive(arr, depth=1):
    if len(arr) <= 1:
        return arr, 0, depth

    mid = len(arr) // 2

    left, comp_left, depth_left = merge_sort_recursive(arr[:mid], depth + 1)
    right, comp_right, depth_right = merge_sort_recursive(arr[mid:], depth + 1)

    merged, comp_merge = merge(left, right)

    total_comp = comp_left + comp_right + comp_merge
    max_depth = max(depth_left, depth_right)

    return merged, total_comp, max_depth


# 🔹 ИТЕРАЦИОННАЯ ВЕРСИЯ (bottom-up)
def merge_sort_iterative(arr):
    a = arr.copy()
    n = len(a)
    temp = [0] * n
    width = 1
    comparisons = 0
    passes = 0

    while width < n:
        passes += 1

        for i in range(0, n, 2 * width):
            left = i
            mid = min(i + width, n)
            right = min(i + 2 * width, n)

            i1, i2 = left, mid
            k = left

            while i1 < mid and i2 < right:
                comparisons += 1
                if a[i1] <= a[i2]:
                    temp[k] = a[i1]
                    i1 += 1
                else:
                    temp[k] = a[i2]
                    i2 += 1
                k += 1

            while i1 < mid:
                temp[k] = a[i1]
                i1 += 1
                k += 1

            while i2 < right:
                temp[k] = a[i2]
                i2 += 1
                k += 1

        a = temp.copy()
        width *= 2

    return a, comparisons, passes


# ДАННЫЕ
cargo_priority = [42, 17, 93, 58, 11, 76, 24, 65, 39, 88, 5, 71, 30, 54, 19, 93, 7, 80, 80, 48, 77, 98, 97, 56, 27, 94, 73, 74, 72, 47, 95, 70, 96, 93, 84, 53, 38, 90, 94, 85, 34, 88, 56, 29, 65, 84, 72, 60, 63, 59, 61, 61, 14, 42, 89, 97, 62, 27, 19, 36, 18, 89, 3, 64, 99, 38, 26, 99, 55, 40, 32, 99, 86, 44, 1, 100, 53, 74, 78, 68, 21, 24, 85, 32, 99, 68, 85, 12, 4, 18, 69, 46, 46, 50, 64, 7, 68, 27, 98, 77, 41, 76, 12, 12, 62, 75, 29, 52, 12, 91, 73, 14, 22, 47, 47, 16, 25, 64, 54, 66, 89, 20, 68, 82, 4, 7, 58, 42, 13, 3, 60, 10, 52, 25, 98, 64, 86, 48, 44, 38, 2, 33, 14, 28, 29, 40, 23, 83, 47, 35]


def run():
    print("Исходный массив:")
    print(cargo_priority)

    # Рекурсивная
    res, comp, depth = merge_sort_recursive(cargo_priority)
    print("\nРекурсивная сортировка слиянием:")
    print("Отсортированный:", res)
    print(f"Сравнения: {comp}, Макс. глубина рекурсии: {depth}")

    # Итерационная
    res, comp, passes = merge_sort_iterative(cargo_priority)
    print("\nИтерационная сортировка слиянием:")
    print("Отсортированный:", res)
    print(f"Сравнения: {comp}, Проходы: {passes}")


run()