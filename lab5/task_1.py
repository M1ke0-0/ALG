def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    comparisons = 0
    swaps = 0
    passes = 0

    for i in range(n):
        passes += 1
        for j in range(0, n - i - 1):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1

    return a, comparisons, swaps, passes


def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    comparisons = 0
    swaps = 0
    passes = 0

    for i in range(n):
        passes += 1
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_index]:
                min_index = j
        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]
            swaps += 1

    return a, comparisons, swaps, passes


def insertion_sort(arr):
    a = arr.copy()
    comparisons = 0
    shifts = 0
    passes = 0

    for i in range(1, len(a)):
        passes += 1
        key = a[i]
        j = i - 1

        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                shifts += 1
                j -= 1
            else:
                break

        a[j + 1] = key

    return a, comparisons, shifts, passes


# Данные
data_sets = {
    "Случайный": [57, 12, 89, 34, 76, 11, 90, 43, 65, 28, 71, 5, 39, 84, 22],
    "Отсортированный": [5, 11, 12, 22, 28, 34, 39, 43, 57, 65, 71, 76, 84, 89, 90],
    "Обратный": [90, 89, 84, 76, 71, 65, 57, 43, 39, 34, 28, 22, 12, 11, 5],
    "Почти отсортированный": [5, 11, 12, 22, 28, 34, 43, 39, 57, 65, 71, 76, 84, 89, 90]
}


def run_tests():
    for name, data in data_sets.items():
        print(f"\n=== {name} массив ===")
        print("Исходный:", data)

        # Пузырьковая
        sorted_arr, comp, swaps, passes = bubble_sort(data)
        print("\nПузырьковая сортировка:")
        print("Отсортированный:", sorted_arr)
        print(f"Сравнения: {comp}, Обмены: {swaps}, Проходы: {passes}")

        # Выбором
        sorted_arr, comp, swaps, passes = selection_sort(data)
        print("\nСортировка выбором:")
        print("Отсортированный:", sorted_arr)
        print(f"Сравнения: {comp}, Обмены: {swaps}, Проходы: {passes}")

        # Вставками
        sorted_arr, comp, shifts, passes = insertion_sort(data)
        print("\nСортировка вставками:")
        print("Отсортированный:", sorted_arr)
        print(f"Сравнения: {comp}, Сдвиги: {shifts}, Проходы: {passes}")


run_tests()