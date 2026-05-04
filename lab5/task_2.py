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


def cocktail_sort(arr):
    a = arr.copy()
    left = 0
    right = len(a) - 1
    comparisons = 0
    swaps = 0
    passes = 0

    while left < right:
        passes += 1

        # проход слева направо
        for i in range(left, right):
            comparisons += 1
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swaps += 1
        right -= 1

        # проход справа налево
        for i in range(right, left, -1):
            comparisons += 1
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
                swaps += 1
        left += 1

    return a, comparisons, swaps, passes


def gnome_sort(arr):
    a = arr.copy()
    i = 0
    comparisons = 0
    swaps = 0
    steps = 0

    while i < len(a):
        steps += 1
        if i == 0:
            i += 1
        comparisons += 1
        if a[i] >= a[i - 1]:
            i += 1
        else:
            a[i], a[i - 1] = a[i - 1], a[i]
            swaps += 1
            i -= 1

    return a, comparisons, swaps, steps


# Данные
data_sets = {
    "data1": [1, 2, 3, 4, 6, 5, 7, 8, 9, 10],
    "data2": [2, 1, 3, 4, 5, 6, 7, 8, 10, 9],
    "data3": [1, 3, 2, 4, 5, 7, 6, 8, 10, 9],
    "data4": [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
}


def run_tests():
    for name, data in data_sets.items():
        print(f"\n=== {name} ===")
        print("Исходный:", data)

        # Пузырьковая
        res, comp, swaps, passes = bubble_sort(data)
        print("\nПузырьковая:")
        print("Результат:", res)
        print(f"Сравнения: {comp}, Перестановки: {swaps}, Проходы: {passes}")

        # Перемешиванием
        res, comp, swaps, passes = cocktail_sort(data)
        print("\nПеремешиванием:")
        print("Результат:", res)
        print(f"Сравнения: {comp}, Перестановки: {swaps}, Проходы: {passes}")

        # Гномья
        res, comp, swaps, steps = gnome_sort(data)
        print("\nГномья сортировка:")
        print("Результат:", res)
        print(f"Сравнения: {comp}, Перестановки: {swaps}, Шаги: {steps}")


run_tests()