"""
Лабораторная работа 2 — Задание 5
Быстрое возведение в степень: итеративный и рекурсивный подходы
(алгоритм «разделяй и властвуй»)
"""

import time


# ─── Наивный итеративный подход O(n) ─────────────────────────────────────────

def power_naive(base: float, exp: int) -> float:
    """Последовательное умножение — O(n) операций."""
    if exp == 0:
        return 1
    result = 1
    for _ in range(exp):
        result *= base
    return result


# ─── Итеративный алгоритм быстрого возведения в степень O(log n) ─────────────

def power_fast_loop(base: float, exp: int) -> float:
    """Быстрое возведение в степень итеративно — O(log n).

    Идея: если показатель чётный, base^n = (base^2)^(n/2).
          если показатель нечётный, base^n = base * base^(n-1).
    """
    if exp == 0:
        return 1
    result = 1
    while exp > 0:
        if exp % 2 == 1:           # нечётная степень
            result *= base
        base *= base
        exp //= 2
    return result


# ─── Рекурсивный алгоритм быстрого возведения в степень O(log n) ─────────────

def power_fast_recursive(base: float, exp: int) -> float:
    """Быстрое возведение в степень рекурсивно — O(log n).

    Терминальный случай: exp == 0 → 1, exp == 1 → base.
    Рекурсивный шаг:
        чётная степень  → (base^(n//2))^2
        нечётная степень → base * base^(n-1)
    """
    if exp == 0:       # ← терминальная часть
        return 1
    if exp == 1:       # ← терминальная часть
        return base

    if exp % 2 == 0:   # ← рекурсивный шаг (чётная)
        half = power_fast_recursive(base, exp // 2)
        return half * half
    else:              # ← рекурсивный шаг (нечётная)
        return base * power_fast_recursive(base, exp - 1)


# ─── Проверка корректности ────────────────────────────────────────────────────

test_cases = [(2, 0), (2, 1), (2, 10), (3, 5), (5, 8), (2, 20)]
print("Проверка корректности:")
print(f"{'base^exp':<12}  {'naive':>15}  {'fast_loop':>12}  {'fast_rec':>12}  {'ok'}")
print("-" * 60)
for b, e in test_cases:
    n = power_naive(b, e)
    fl = power_fast_loop(b, e)
    fr = power_fast_recursive(b, e)
    ok = "✓" if n == fl == fr else "✗"
    print(f"{f'{b}^{e}':<12}  {n:>15}  {fl:>12}  {fr:>12}  {ok}")

# ─── Замер производительности ─────────────────────────────────────────────────

REPEATS = 50_000
BASE = 2

print("\nЗамер производительности (base=2, среднее время на вызов, мкс):")
print(f"{'exp':>10}  {'naive':>12}  {'fast_loop':>12}  {'fast_rec':>12}")
print("-" * 55)

for exp in [10, 100, 1_000, 10_000, 100_000]:
    def bench(func, reps=REPEATS):
        t = time.perf_counter()
        for _ in range(reps):
            func(BASE, exp)
        return (time.perf_counter() - t) / reps * 1_000_000

    t_naive = bench(power_naive) if exp <= 10_000 else float("inf")
    t_fl    = bench(power_fast_loop)
    t_fr    = bench(power_fast_recursive)

    naive_str = f"{t_naive:.3f}" if exp <= 10_000 else "очень долго"
    print(f"{exp:>10}  {naive_str:>12}  {t_fl:>12.3f}  {t_fr:>12.3f}")

print("""
─── Вывод ────────────────────────────────────────────────────────
  • Наивный алгоритм: O(n) умножений — при большой степени медленно.
  • Быстрый алгоритм («разделяй и властвуй»): O(log n) умножений.
    При exp=1 000 000 наивный делает 1 000 000 умножений,
    быстрый — всего ~20.
  • Итеративная и рекурсивная версии Fast Power примерно одинаковы
    по скорости; итеративная чуть быстрее из-за отсутствия оверхеда
    на создание фреймов стека.
──────────────────────────────────────────────────────────────────
""")
