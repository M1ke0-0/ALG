"""
Лабораторная работа 2 — Задание 2
Факториал: итеративный и рекурсивный подходы
"""

import time
import sys

# ─── Реализации ───────────────────────────────────────────────────────────────

def factorial_loop(n: int) -> int:
    """Факториал через цикл (итеративно)."""
    if n < 0:
        raise ValueError("Факториал определён только для неотрицательных чисел")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    """Факториал через рекурсию.
    Терминальный случай: n == 0 или n == 1 → возвращает 1.
    Рекурсивный шаг: n * factorial_recursive(n - 1).
    """
    if n < 0:
        raise ValueError("Факториал определён только для неотрицательных чисел")
    if n == 0 or n == 1:   # ← терминальная часть
        return 1
    return n * factorial_recursive(n - 1)  # ← рекурсивный шаг


# ─── Вспомогательная функция замера времени ──────────────────────────────────

def measure(func, n: int, repeats: int = 10_000) -> float:
    """Возвращает среднее время одного вызова в микросекундах."""
    start = time.perf_counter()
    for _ in range(repeats):
        func(n)
    elapsed = time.perf_counter() - start
    return elapsed / repeats * 1_000_000  # мкс


# ─── Проверка корректности ────────────────────────────────────────────────────

test_values = [0, 1, 5, 10, 20]
print("Проверка корректности:")
print(f"{'n':>5}  {'loop':>25}  {'recursive':>25}  {'совпадают':>10}")
print("-" * 70)
for n in test_values:
    fl = factorial_loop(n)
    fr = factorial_recursive(n)
    print(f"{n:>5}  {fl:>25}  {fr:>25}  {'✓' if fl == fr else '✗':>10}")

# ─── Замер производительности ─────────────────────────────────────────────────

print("\nЗамер производительности (среднее время, мкс):")
print(f"{'n':>6}  {'loop (мкс)':>14}  {'recursive (мкс)':>17}  {'быстрее':>10}")
print("-" * 55)
bench_values = [5, 10, 50, 100, 500]
for n in bench_values:
    t_loop = measure(factorial_loop, n)
    t_rec  = measure(factorial_recursive, n)
    faster = "loop" if t_loop <= t_rec else "recursive"
    print(f"{n:>6}  {t_loop:>14.3f}  {t_rec:>17.3f}  {faster:>10}")

# ─── factorial(1000) ──────────────────────────────────────────────────────────

print("\n--- factorial(1000) ---")

# Итеративный — никаких проблем
result_loop = factorial_loop(1000)
print(f"loop: ...{str(result_loop)[-20:]} (последние 20 цифр), длина = {len(str(result_loop))} цифр")

# Рекурсивный — может упасть из-за лимита стека
sys.setrecursionlimit(10_000)   # увеличиваем лимит
try:
    result_rec = factorial_recursive(1000)
    print(f"recursive: ...{str(result_rec)[-20:]} (успешно при увеличенном лимите стека)")
except RecursionError as e:
    print(f"recursive: RecursionError — {e}")

print(f"\nТекущий лимит рекурсии: {sys.getrecursionlimit()}")

print("""
─── Вывод ────────────────────────────────────────────────────────
  • Итеративный подход использует O(1) памяти стека, работает
    быстро и не имеет ограничений по глубине.
  • Рекурсивный — создаёт отдельный фрейм стека для каждого
    вызова. При n=1000 глубина достигает 1000 фреймов.
  • По умолчанию Python ограничивает глубину рекурсии (1000).
    Превышение вызывает RecursionError.
  • Для случаев с большой глубиной рекурсии (n > ~900)
    предпочтительнее итеративный подход.
──────────────────────────────────────────────────────────────────
""")
