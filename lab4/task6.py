"""
Задание 6. Влияние размера массива на эффективность алгоритмов поиска.
N = 10^3, 10^4, 10^5, 10^6
"""

import time
import random
import math
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


# ── Алгоритмы поиска ──────────────────────────────────────────────────────────

def linear_search_barrier(arr, target):
    n = len(arr)
    arr_copy = arr + [target]
    i = 0
    while arr_copy[i] != target:
        i += 1
    return i if i < n else -1


def binary_search(arr, target):
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


def interpolation_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi and arr[lo] <= target <= arr[hi]:
        if arr[lo] == arr[hi]:
            return lo if arr[lo] == target else -1
        pos = lo + (target - arr[lo]) * (hi - lo) // (arr[hi] - arr[lo])
        pos = max(lo, min(hi, pos))
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            lo = pos + 1
        else:
            hi = pos - 1
    return -1


def exponential_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] == target:
        return 0
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    lo, hi = i // 2, min(i, n - 1)
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


# ── Измерение среднего времени одного поиска ──────────────────────────────────

def avg_time_ms(func, arr, queries):
    t0 = time.perf_counter()
    for q in queries:
        func(arr, q)
    elapsed = time.perf_counter() - t0
    return elapsed / len(queries) * 1_000   # мс на один запрос


# ── Основная функция ──────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("ЗАДАНИЕ 6: Влияние размера массива на время поиска")
    print("=" * 60)

    random.seed(42)
    Ns = [1_000, 10_000, 100_000, 1_000_000]
    NUM_QUERIES = 200      # запросов на каждый N

    algorithms = [
        ("Линейный (барьер)", linear_search_barrier),
        ("Бинарный",          binary_search),
        ("Интерполяционный",  interpolation_search),
        ("Экспоненциальный",  exponential_search),
    ]

    # словарь результатов: {name -> [t_N1, t_N2, ...]}
    results = {name: [] for name, _ in algorithms}

    print(f"\n{'N':>10}", end="")
    for name, _ in algorithms:
        print(f" | {name:>18}", end="")
    print()
    print("-" * 85)

    for N in Ns:
        # равномерный отсортированный массив (хорошо для интерполяции)
        arr = list(range(0, N * 2, 2))   # чётные числа 0, 2, 4, ... 2N-2
        # запросы: 50% из массива, 50% отсутствуют
        exist = random.choices(arr, k=NUM_QUERIES // 2)
        miss  = [arr[-1] + random.randint(1, 100) for _ in range(NUM_QUERIES // 2)]
        queries = exist + miss
        random.shuffle(queries)

        row_times = []
        for name, func in algorithms:
            t = avg_time_ms(func, arr, queries)
            results[name].append(t)
            row_times.append(t)

        print(f"{N:>10}", end="")
        for t in row_times:
            print(f" | {t:>16.6f} мс", end="")
        print()

    # ── График ───────────────────────────────────────────────────────────────
    colors = ['#E74C3C', '#2980B9', '#27AE60', '#8E44AD']
    markers = ['o', 's', '^', 'D']

    fig, ax = plt.subplots(figsize=(11, 7))

    for (name, _), color, marker in zip(algorithms, colors, markers):
        ax.plot(Ns, results[name], label=name, color=color,
                marker=marker, linewidth=2, markersize=7)

    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('Размер массива N (лог. шкала)', fontsize=12)
    ax.set_ylabel('Среднее время одного поиска (мс, лог. шкала)', fontsize=12)
    ax.set_title('Задание 6: Зависимость времени поиска от размера массива', fontsize=13)
    ax.legend(fontsize=11)
    ax.grid(True, which='both', alpha=0.3)
    ax.set_xticks(Ns)
    ax.set_xticklabels([f'10^{int(math.log10(n))}' for n in Ns], fontsize=11)
    plt.tight_layout()
    plt.savefig('task6_size_effect.png', dpi=150)
    print("\n✓ График сохранён: task6_size_effect.png")

    print("\nВывод:")
    print("  • Линейный поиск: время растёт ~линейно O(n).")
    print("  • Бинарный поиск: O(log n) — рост почти незаметен на графике.")
    print("  • Интерполяционный: O(log log n) при равномерных данных — самый быстрый.")
    print("  • Экспоненциальный: O(log n), схож с бинарным, но полезен для")
    print("    неограниченных массивов — сначала быстро находит диапазон.")


if __name__ == "__main__":
    main()
