"""
Задание 2. Исследование интерполяционного поиска
на массивах с различным распределением значений:
  - равномерное
  - квадратичное
  - экспоненциальное
  - случайные отсортированные данные с перекосами
"""

import time
import random
import math
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


# ── Алгоритмы поиска ──────────────────────────────────────────────────────────

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


# ── Генераторы распределений ──────────────────────────────────────────────────

def generate_uniform(n: int) -> list:
    """Равномерное: xi = i, шаг 1"""
    return list(range(n))


def generate_quadratic(n: int) -> list:
    """Квадратичное: xi = i²"""
    return [i * i for i in range(n)]


def generate_exponential(n: int) -> list:
    """Экспоненциальное: xi = round(e^(i * 10/n))"""
    return sorted(set(int(math.exp(i * 10.0 / n)) for i in range(n)))


def generate_skewed(n: int) -> list:
    """Случайные с перекосом: большинство значений сгруппированы у 0"""
    vals = sorted(int(random.expovariate(0.01)) for _ in range(n))
    return vals


# ── Измерение времени ─────────────────────────────────────────────────────────

def measure_time(func, arr, queries, repeats=5):
    total = 0.0
    for _ in range(repeats):
        t0 = time.perf_counter()
        for q in queries:
            func(arr, q)
        total += time.perf_counter() - t0
    return total / repeats


# ── Основная функция ──────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("ЗАДАНИЕ 2: Интерполяционный поиск на разных распределениях")
    print("=" * 60)

    N = 10_000
    NUM_QUERIES = 500
    random.seed(42)

    distributions = {
        "Равномерное":     generate_uniform(N),
        "Квадратичное":    generate_quadratic(N),
        "Экспоненциальное": generate_exponential(N),
        "Перекос (скос)":  generate_skewed(N),
    }

    results_interp = {}
    results_binary = {}

    print(f"\n{'Распределение':<22} | {'Интерполяц. (мс)':>18} | {'Бинарный (мс)':>15} | {'Ускорение':>10}")
    print("-" * 74)

    for name, arr in distributions.items():
        if len(arr) < 2:
            arr = list(range(N))
        # запросы — случайные элементы из массива (50%) + несуществующие (50%)
        exist = random.choices(arr, k=NUM_QUERIES // 2)
        miss  = [arr[-1] + random.randint(1, 1000) for _ in range(NUM_QUERIES // 2)]
        queries = exist + miss
        random.shuffle(queries)

        t_interp = measure_time(interpolation_search, arr, queries) * 1000
        t_binary = measure_time(binary_search,        arr, queries) * 1000

        results_interp[name] = t_interp
        results_binary[name] = t_binary

        ratio = t_binary / t_interp if t_interp > 0 else float('inf')
        print(f"{name:<22} | {t_interp:>18.3f} | {t_binary:>15.3f} | {ratio:>10.2f}x")

    # ── График ───────────────────────────────────────────────────────────────
    names = list(distributions.keys())
    x = range(len(names))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    bars1 = ax.bar([i - width/2 for i in x], [results_interp[n] for n in names],
                   width, label='Интерполяционный', color='#4C72B0', alpha=0.85)
    bars2 = ax.bar([i + width/2 for i in x], [results_binary[n] for n in names],
                   width, label='Бинарный', color='#DD8452', alpha=0.85)

    ax.set_xlabel('Вид распределения', fontsize=12)
    ax.set_ylabel('Среднее время (мс)', fontsize=12)
    ax.set_title('Задание 2: Интерполяционный vs Бинарный поиск\nна разных распределениях', fontsize=13)
    ax.set_xticks(list(x))
    ax.set_xticklabels(names, fontsize=10)
    ax.legend(fontsize=11)
    ax.bar_label(bars1, fmt='%.3f', padding=3, fontsize=8)
    ax.bar_label(bars2, fmt='%.3f', padding=3, fontsize=8)
    plt.tight_layout()
    plt.savefig('task2_distributions.png', dpi=150)
    print("\n✓ График сохранён: task2_distributions.png")

    print("\nВывод:")
    print("  • На равномерных данных интерполяционный поиск быстрее бинарного,")
    print("    т.к. формула интерполяции точно предсказывает позицию элемента.")
    print("  • На квадратичных/экспоненциальных/скошенных данных эффективность падает,")
    print("    т.к. предсказанная позиция далеко от реальной — нужно больше итераций.")


if __name__ == "__main__":
    main()
