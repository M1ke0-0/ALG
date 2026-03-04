"""
Лабораторная работа 1: Анализ алгоритмов и асимптотическая сложность
"""

import time
import random
import math
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['figure.facecolor'] = '#1e1e2e'
plt.rcParams['axes.facecolor'] = '#2a2a3e'
plt.rcParams['axes.edgecolor'] = '#555577'
plt.rcParams['axes.labelcolor'] = '#cdd6f4'
plt.rcParams['xtick.color'] = '#cdd6f4'
plt.rcParams['ytick.color'] = '#cdd6f4'
plt.rcParams['text.color'] = '#cdd6f4'
plt.rcParams['grid.color'] = '#44475a'
plt.rcParams['grid.alpha'] = 0.5
plt.rcParams['legend.facecolor'] = '#313244'
plt.rcParams['legend.edgecolor'] = '#555577'

# ============================================================
# ЗАДАНИЕ 3: Эксперимент с пузырьковой сортировкой
# ============================================================

def bubble_sort(arr):
    """Пузырьковая сортировка O(n²)"""
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def measure_time(sort_func, arr, repeats=5):
    """Измерение среднего времени выполнения за repeats повторов"""
    times = []
    for _ in range(repeats):
        data = arr.copy()
        start = time.perf_counter()
        sort_func(data)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / len(times)


print("=" * 60)
print("ЗАДАНИЕ 3: Эксперимент с пузырьковой сортировкой")
print("=" * 60)

sizes_task3 = [100, 200, 400, 800, 1600, 3200]
times_bubble = []

for n in sizes_task3:
    arr = [random.randint(0, 10000) for _ in range(n)]
    t = measure_time(bubble_sort, arr, repeats=5)
    times_bubble.append(t)
    print(f"  n={n:5d}  среднее время={t*1000:.4f} мс")

# --- График 3а: время от n ---
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Задание 3: Пузырьковая сортировка', fontsize=15, fontweight='bold',
             color='#cba6f7')

axes[0].plot(sizes_task3, [t * 1000 for t in times_bubble],
             'o-', color='#f38ba8', linewidth=2.5, markersize=8, label='Bubble Sort')
axes[0].set_xlabel('Размер массива n')
axes[0].set_ylabel('Время (мс)')
axes[0].set_title('Зависимость времени от n')
axes[0].legend()
axes[0].grid(True)

# --- График 3б: время от n² ---
n2_values = [n**2 for n in sizes_task3]
axes[1].plot(n2_values, [t * 1000 for t in times_bubble],
             'o-', color='#a6e3a1', linewidth=2.5, markersize=8, label='Bubble Sort')
axes[1].set_xlabel('n²')
axes[1].set_ylabel('Время (мс)')
axes[1].set_title('Зависимость времени от n²\n(должна быть близка к прямой)')
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.savefig('E:/Labi_ALG/task3_bubble.png', dpi=150, bbox_inches='tight')
plt.show()
print("  [OK] График сохранён: task3_bubble.png")

# ============================================================
# ЗАДАНИЕ 4: Сравнение O(n²) и O(n log n)
# ============================================================

print()
print("=" * 60)
print("ЗАДАНИЕ 4: Сравнение Bubble Sort vs Python sorted()")
print("=" * 60)

sizes_task4 = [1000, 2000, 5000, 10000]
times_bubble4 = []
times_sorted4 = []

for n in sizes_task4:
    arr = [random.randint(0, 100000) for _ in range(n)]

    tb = measure_time(bubble_sort, arr, repeats=5)
    ts = measure_time(lambda a: sorted(a), arr, repeats=5)

    times_bubble4.append(tb)
    times_sorted4.append(ts)
    print(f"  n={n:6d} | bubble={tb*1000:8.3f} мс | sorted={ts*1000:8.3f} мс | "
          f"ratio={tb/ts:.1f}x")

fig2, ax = plt.subplots(figsize=(10, 6))
fig2.suptitle('Задание 4: Bubble Sort O(n²) vs sorted() O(n log n)',
              fontsize=14, fontweight='bold', color='#cba6f7')

ax.plot(sizes_task4, [t * 1000 for t in times_bubble4],
        'o-', color='#f38ba8', linewidth=2.5, markersize=8, label='Bubble Sort O(n²)')
ax.plot(sizes_task4, [t * 1000 for t in times_sorted4],
        's-', color='#89b4fa', linewidth=2.5, markersize=8, label='sorted() O(n log n)')

ax.set_xlabel('Размер массива n')
ax.set_ylabel('Время (мс)')
ax.set_title('Сравнение времени выполнения')
ax.legend()
ax.grid(True)

plt.tight_layout()
plt.savefig('E:/Labi_ALG/task4_comparison.png', dpi=150, bbox_inches='tight')
plt.show()
print("  [OK] График сохранён: task4_comparison.png")

# ============================================================
# ЗАДАНИЕ 5: Оценка времени масштабирования
# ============================================================

print()
print("=" * 60)
print("ЗАДАНИЕ 5: Оценка времени масштабирования")
print("=" * 60)

n1 = 1_000_000
t1 = 120  # мс
n2 = 4_000_000

# T(n) = C * n * log2(n)
# T(n2)/T(n1) = (n2 * log2(n2)) / (n1 * log2(n1))
ratio = (n2 * math.log2(n2)) / (n1 * math.log2(n1))
t2 = t1 * ratio

print(f"  n1 = {n1:,},  T(n1) = {t1} мс")
print(f"  n2 = {n2:,}")
print(f"  Коэффициент = (n2·log₂n2) / (n1·log₂n1)")
print(f"             = ({n2}·{math.log2(n2):.2f}) / ({n1}·{math.log2(n1):.2f})")
print(f"             = {ratio:.4f}")
print(f"  T(n2) ≈ {t1} × {ratio:.4f} ≈ {t2:.2f} мс ≈ {t2/1000:.3f} с")

print()
print("Все вычисления завершены!")
