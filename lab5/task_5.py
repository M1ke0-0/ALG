import copy

# ---------- АЛГОРИТМЫ ----------

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j][1] > a[j + 1][1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j][1] > key[1]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if a[j][1] < a[min_i][1]:
                min_i = j
        a[i], a[min_i] = a[min_i], a[i]
    return a


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][1]
    left = [x for x in arr if x[1] < pivot]
    middle = [x for x in arr if x[1] == pivot]
    right = [x for x in arr if x[1] > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# ---------- ПРОВЕРКА УСТОЙЧИВОСТИ ----------

def is_stable(original, sorted_arr):
    positions = {}

    for i, item in enumerate(original):
        key = item[1]
        if key not in positions:
            positions[key] = []
        positions[key].append(item[0])

    for key in positions:
        original_order = positions[key]
        sorted_order = [x[0] for x in sorted_arr if x[1] == key]

        if original_order != sorted_order:
            return False

    return True


# ---------- ДАННЫЕ ----------

records1 = [("A1",4),("A2",2),("A3",4),("A4",1),("A5",3),("A6",2),("A7",4),("A8",1),("A9",3),("A10",2)]
records2 = [("B1",5),("B2",5),("B3",5),("B4",2),("B5",2),("B6",3),("B7",3),("B8",3),("B9",1),("B10",1)]
records3 = [("C1",3),("C2",1),("C3",3),("C4",2),("C5",3),("C6",1),("C7",2),("C8",3),("C9",1),("C10",2),("C11",3),("C12",1)]

datasets = {
    "records1": records1,
    "records2": records2,
    "records3": records3
}


# ---------- ЗАПУСК ----------

def run():
    algorithms = {
        "Bubble": bubble_sort,
        "Insertion": insertion_sort,
        "Selection": selection_sort,
        "Quick": quick_sort
    }

    for name, data in datasets.items():
        print(f"\n=== {name} ===")
        print("Исходный:", data)

        for alg_name, func in algorithms.items():
            result = func(data)
            stable = is_stable(data, result)

            print(f"\n{alg_name}:")
            print("Результат:", result)
            print("Устойчивость:", "Да" if stable else "Нет")


# ---------- МНОГОКРИТЕРИАЛЬНАЯ СОРТИРОВКА ----------

def multi_sort_demo(data):
    print("\n=== Многокритериальная сортировка ===")
    print("Исходный:", data)

    # 1. сортировка по идентификатору
    step1 = sorted(data, key=lambda x: x[0])

    # 2. сортировка по ключу
    stable_result = insertion_sort(step1)
    unstable_result = selection_sort(step1)

    print("\nПосле сортировки по ID:")
    print(step1)

    print("\nУстойчивая сортировка (вставки):")
    print(stable_result)

    print("\nНеустойчивая сортировка (выбор):")
    print(unstable_result)


run()
multi_sort_demo(records1)