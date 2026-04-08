"""
Задание 4. Подсчёт внутренних характеристик алгоритмов:
  - количество сравнений с искомым элементом
  - количество итераций основного цикла
  - количество сдвигов границ / изменений индексов
"""


# ── Алгоритмы со статистикой ──────────────────────────────────────────────────

def linear_barrier_stats(arr: list, target) -> dict:
    """Модифицированный линейный поиск (с барьером) + статистика."""
    n = len(arr)
    arr_copy = arr + [target]
    comparisons = 0
    iterations  = 0
    i = 0
    while True:
        iterations  += 1
        comparisons += 1
        if arr_copy[i] == target:
            break
        i += 1
    found_index = i if i < n else -1
    return {
        "index":       found_index,
        "comparisons": comparisons,
        "iterations":  iterations,
        "shifts":      i,          # число шагов указателя i
    }


def binary_search_stats(arr: list, target) -> dict:
    """Бинарный поиск + статистика."""
    lo, hi = 0, len(arr) - 1
    comparisons = 0
    iterations  = 0
    shifts      = 0
    result      = -1
    while lo <= hi:
        iterations  += 1
        mid          = (lo + hi) // 2
        comparisons += 1
        if arr[mid] == target:
            result = mid
            break
        elif arr[mid] < target:
            lo = mid + 1
            shifts += 1
        else:
            hi = mid - 1
            shifts += 1
    return {
        "index":       result,
        "comparisons": comparisons,
        "iterations":  iterations,
        "shifts":      shifts,
    }


def interpolation_search_stats(arr: list, target) -> dict:
    """Интерполяционный поиск + статистика."""
    lo, hi = 0, len(arr) - 1
    comparisons = 0
    iterations  = 0
    shifts      = 0
    result      = -1
    while lo <= hi and arr[lo] <= target <= arr[hi]:
        iterations  += 1
        if arr[lo] == arr[hi]:
            comparisons += 1
            if arr[lo] == target:
                result = lo
            break
        pos = lo + (target - arr[lo]) * (hi - lo) // (arr[hi] - arr[lo])
        pos = max(lo, min(hi, pos))
        comparisons += 1
        if arr[pos] == target:
            result = pos
            break
        elif arr[pos] < target:
            lo = pos + 1
            shifts += 1
        else:
            hi = pos - 1
            shifts += 1
    return {
        "index":       result,
        "comparisons": comparisons,
        "iterations":  iterations,
        "shifts":      shifts,
    }


def exponential_search_stats(arr: list, target) -> dict:
    """Экспоненциальный поиск + статистика."""
    n = len(arr)
    comparisons = 0
    iterations  = 0
    shifts      = 0

    if n == 0:
        return {"index": -1, "comparisons": 0, "iterations": 0, "shifts": 0}

    comparisons += 1
    if arr[0] == target:
        return {"index": 0, "comparisons": 1, "iterations": 1, "shifts": 0}

    # экспоненциальное расширение
    i = 1
    while i < n and arr[i] <= target:
        iterations  += 1
        comparisons += 1
        shifts      += 1
        i *= 2

    # бинарный поиск в диапазоне
    lo = i // 2
    hi = min(i, n - 1)
    result = -1
    while lo <= hi:
        iterations  += 1
        mid          = (lo + hi) // 2
        comparisons += 1
        if arr[mid] == target:
            result = mid
            break
        elif arr[mid] < target:
            lo = mid + 1
            shifts += 1
        else:
            hi = mid - 1
            shifts += 1
    return {
        "index":       result,
        "comparisons": comparisons,
        "iterations":  iterations,
        "shifts":      shifts,
    }


# ── Основная функция ──────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("ЗАДАНИЕ 4: Внутренние характеристики алгоритмов поиска")
    print("=" * 60)

    import random
    random.seed(0)

    datasets = {
        "Начало (лучший случай)":    0,
        "Середина":                  499,
        "Конец (худший для линейн.)": 999,
        "Отсутствует":               -1,   # специальный маркер
    }

    arr = list(range(1000))   # [0..999]
    missing_val = 1500

    algorithms = [
        ("Линейный (барьер)", linear_barrier_stats),
        ("Бинарный",          binary_search_stats),
        ("Интерполяционный",  interpolation_search_stats),
        ("Экспоненциальный",  exponential_search_stats),
    ]

    for case_name, target_key in datasets.items():
        target = target_key if target_key != -1 else missing_val
        print(f"\n► Случай: «{case_name}» (ищем {target})")
        print(f"  {'Алгоритм':<22} | {'Результат':>10} | {'Сравнений':>10} | {'Итераций':>10} | {'Сдвигов':>10}")
        print("  " + "-" * 72)
        for name, func in algorithms:
            stats = func(arr, target)
            idx_str = str(stats['index']) if stats['index'] != -1 else "не найден"
            print(f"  {name:<22} | {idx_str:>10} | {stats['comparisons']:>10} | "
                  f"{stats['iterations']:>10} | {stats['shifts']:>10}")

    # ── Средние значения по случайным запросам ────────────────────────────────
    print("\n\n► Средние характеристики (1000 случайных запросов, N=1000)")
    queries = [random.randint(0, 1999) for _ in range(1000)]
    print(f"  {'Алгоритм':<22} | {'Сравнений':>10} | {'Итераций':>10} | {'Сдвигов':>10}")
    print("  " + "-" * 58)
    for name, func in algorithms:
        total_cmp = total_it = total_sh = 0
        for q in queries:
            s = func(arr, q)
            total_cmp += s['comparisons']
            total_it  += s['iterations']
            total_sh  += s['shifts']
        n = len(queries)
        print(f"  {name:<22} | {total_cmp/n:>10.2f} | {total_it/n:>10.2f} | {total_sh/n:>10.2f}")

    print("\nВывод:")
    print("  • Число сравнений — «чистая» характеристика, не зависит от CPU/ОС.")
    print("  • Бинарный/экспоненциальный делают O(log n) сравнений независимо")
    print("    от распределения данных.")
    print("  • Интерполяционный делает меньше сравнений при равномерных данных.")
    print("  • Линейный в худшем случае делает N сравнений.")


if __name__ == "__main__":
    main()
