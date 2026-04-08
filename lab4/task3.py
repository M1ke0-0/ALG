"""
Задание 3. Порог, при котором выгоднее сортировать массив
и использовать бинарный поиск, чем K раз выполнять линейный поиск.

Сравниваем:
  Linear total  = K * T_linear
  Sort + Binary = T_sort + K * T_binary
"""

import time
import random
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


# ── Алгоритмы ─────────────────────────────────────────────────────────────────

def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


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


# ── Измерение ─────────────────────────────────────────────────────────────────

def measure_linear_total(arr, queries):
    """Время K линейных поисков в неотсортированном массиве."""
    t0 = time.perf_counter()
    for q in queries:
        linear_search(arr, q)
    return time.perf_counter() - t0


def measure_sort_binary_total(arr, queries):
    """Время сортировки + K бинарных поисков."""
    t0 = time.perf_counter()
    sorted_arr = sorted(arr)          # однократная сортировка
    for q in queries:
        binary_search(sorted_arr, q)
    return time.perf_counter() - t0


# ── Основная функция ──────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("ЗАДАНИЕ 3: Порог выгодности сортировки + бинарного поиска")
    print("=" * 60)

    N = 10_000          # размер массива
    random.seed(42)
    arr_original = [random.randint(0, 10 * N) for _ in range(N)]

    # Значения K — число поисковых запросов
    K_values = list(range(1, 501, 5))

    times_linear = []
    times_sort_binary = []

    print(f"\nРазмер массива N = {N}")
    print("Измерение для K от 1 до 500 ...", end=" ", flush=True)

    for K in K_values:
        queries = [random.randint(0, 10 * N) for _ in range(K)]

        # линейный: усредняем по нескольким запускам для стабильности
        t_lin = 0.0
        t_sb  = 0.0
        REPEATS = 5
        for _ in range(REPEATS):
            arr = arr_original[:]   # свежая копия (не отсортированная)
            t_lin += measure_linear_total(arr, queries)
            arr2  = arr_original[:]
            t_sb  += measure_sort_binary_total(arr2, queries)
        times_linear.append(t_lin / REPEATS * 1000)
        times_sort_binary.append(t_sb / REPEATS * 1000)

    print("готово.")

    # ── Найти точку пересечения ───────────────────────────────────────────────
    crossover_K = None
    for i, K in enumerate(K_values):
        if times_sort_binary[i] <= times_linear[i]:
            crossover_K = K
            break

    print(f"\n{'K':>6} | {'Linear total (мс)':>18} | {'Sort+Binary total (мс)':>24}")
    print("-" * 55)
    sample_Ks = [1, 5, 10, 20, 50, 100, 200, 300, 400, 500]
    for K in sample_Ks:
        idx = K_values.index(K) if K in K_values else None
        if idx is not None:
            print(f"{K:>6} | {times_linear[idx]:>18.3f} | {times_sort_binary[idx]:>24.3f}")

    if crossover_K:
        print(f"\n✓ Точка пересечения: K ≈ {crossover_K}")
        print(f"  При K > {crossover_K} стратегия «Sort + Binary» выгоднее.")
    else:
        print("\n✓ Sort+Binary всегда медленнее (для данного N сортировка слишком дорога).")

    # ── График ───────────────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(K_values, times_linear,      label='Linear total',      color='#E74C3C', linewidth=2)
    ax.plot(K_values, times_sort_binary, label='Sort + Binary total', color='#2ECC71', linewidth=2)

    if crossover_K:
        ax.axvline(x=crossover_K, color='gray', linestyle='--', alpha=0.7,
                   label=f'Точка перехода K≈{crossover_K}')

    ax.set_xlabel('Число поисковых запросов K', fontsize=12)
    ax.set_ylabel('Суммарное время (мс)', fontsize=12)
    ax.set_title(f'Задание 3: Linear vs Sort+Binary (N={N})', fontsize=13)
    ax.legend(fontsize=11)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig('task3_threshold.png', dpi=150)
    print("\n✓ График сохранён: task3_threshold.png")

    print("\nВывод:")
    print("  • При малом K линейный поиск быстрее — нет затрат на сортировку.")
    print("  • При большом K стоимость сортировки «размазывается» на множество")
    print("    быстрых бинарных поисков и суммарно выгоднее.")


if __name__ == "__main__":
    main()
