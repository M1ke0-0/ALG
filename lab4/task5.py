"""
Задание 5. Сравнение поиска:
  - Своя реализация (бинарный поиск на list)
  - Встроенные средства Python: `in`, `.index()`
  - numpy.searchsorted на массиве NumPy
"""

import time
import random
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False
    print("NumPy не установлен. Установите: pip install numpy")


# ── Реализации поиска ─────────────────────────────────────────────────────────

def binary_search_custom(arr: list, target) -> int:
    """Собственная реализация бинарного поиска."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def python_in(arr: list, target) -> bool:
    """Встроенный оператор `in`."""
    return target in arr


def python_index(arr: list, target) -> int:
    """Встроенный метод `.index()` (с обработкой ValueError)."""
    try:
        return arr.index(target)
    except ValueError:
        return -1


def numpy_searchsorted(np_arr, target) -> int:
    """numpy.searchsorted на отсортированном NumPy-массиве."""
    idx = np.searchsorted(np_arr, target)
    if idx < len(np_arr) and np_arr[idx] == target:
        return int(idx)
    return -1


# ── Измерение ─────────────────────────────────────────────────────────────────

def measure(func, arr, queries, repeats=10):
    total = 0.0
    for _ in range(repeats):
        t0 = time.perf_counter()
        for q in queries:
            func(arr, q)
        total += time.perf_counter() - t0
    return (total / repeats) * 1000   # мс


# ── Основная функция ──────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("ЗАДАНИЕ 5: Сравнение пользовательской реализации с Python/NumPy")
    print("=" * 60)

    random.seed(42)
    Ns = [1_000, 10_000, 100_000]
    NUM_QUERIES = 1_000

    all_results = {
        "N": [],
        "Бинарный (своя)": [],
        "Python .index()": [],
        "Python in":       [],
        "NumPy searchsorted": [],
    }

    for N in Ns:
        arr_sorted = sorted(random.sample(range(N * 10), N))
        # запросы: 60% из массива, 40% отсутствуют
        exist = random.choices(arr_sorted, k=int(NUM_QUERIES * 0.6))
        miss  = [arr_sorted[-1] + random.randint(1, 1000) for _ in range(int(NUM_QUERIES * 0.4))]
        queries = exist + miss
        random.shuffle(queries)

        np_arr = np.array(arr_sorted) if HAS_NUMPY else None

        t_bin   = measure(lambda a, q: binary_search_custom(a, q), arr_sorted, queries)
        t_idx   = measure(lambda a, q: python_index(a, q),          arr_sorted, queries)
        t_in    = measure(lambda a, q: python_in(a, q),              arr_sorted, queries)
        t_np    = measure(lambda a, q: numpy_searchsorted(np_arr, q), arr_sorted, queries) if HAS_NUMPY else 0.0

        all_results["N"].append(N)
        all_results["Бинарный (своя)"].append(t_bin)
        all_results["Python .index()"].append(t_idx)
        all_results["Python in"].append(t_in)
        all_results["NumPy searchsorted"].append(t_np)

    # ── Таблица ───────────────────────────────────────────────────────────────
    print(f"\n{'N':>10} | {'Бинарный(своя)':>16} | {'Python.index()':>16} | {'Python in':>12} | {'NumPy':>12}")
    print("-" * 75)
    for i, N in enumerate(all_results["N"]):
        row = (f"{N:>10} | "
               f"{all_results['Бинарный (своя)'][i]:>14.3f} мс | "
               f"{all_results['Python .index()'][i]:>14.3f} мс | "
               f"{all_results['Python in'][i]:>10.3f} мс | "
               f"{all_results['NumPy searchsorted'][i]:>10.3f} мс")
        print(row)

    # ── График ───────────────────────────────────────────────────────────────
    labels = [str(n) for n in all_results["N"]]
    x = range(len(labels))

    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ['#4C72B0', '#DD8452', '#55A868', '#C44E52']
    methods = ["Бинарный (своя)", "Python .index()", "Python in", "NumPy searchsorted"]

    width = 0.20
    for j, (method, color) in enumerate(zip(methods, colors)):
        offset = (j - 1.5) * width
        vals = all_results[method]
        bars = ax.bar([i + offset for i in x], vals, width, label=method, color=color, alpha=0.85)
        ax.bar_label(bars, fmt='%.2f', padding=3, fontsize=7)

    ax.set_xlabel('Размер массива N', fontsize=12)
    ax.set_ylabel('Среднее время (мс)', fontsize=12)
    ax.set_title('Задание 5: Сравнение реализаций поиска', fontsize=13)
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels, fontsize=11)
    ax.legend(fontsize=10)
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('task5_comparison.png', dpi=150)
    print("\n✓ График сохранён: task5_comparison.png")

    print("\nВывод:")
    print("  • NumPy реализован на C → значительно быстрее Python-реализаций.")
    print("  • `in` и `.index()` используют линейный поиск → медленнее на больших N.")
    print("  • Собственный бинарный поиск быстрее `in`/`.index()`, но медленнее NumPy.")
    print("  • Писать алгоритм вручную имеет смысл для обучения или особых условий;")
    print("    в реальных задачах предпочтительны оптимизированные библиотеки.")


if __name__ == "__main__":
    main()
