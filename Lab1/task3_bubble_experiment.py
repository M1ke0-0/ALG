import time
import random
import matplotlib.pyplot as plt

plt.rcParams['font.family']        = 'DejaVu Sans'
plt.rcParams['figure.facecolor']   = '#1e1e2e'
plt.rcParams['axes.facecolor']     = '#2a2a3e'
plt.rcParams['axes.edgecolor']     = '#555577'
plt.rcParams['axes.labelcolor']    = '#cdd6f4'
plt.rcParams['xtick.color']        = '#cdd6f4'
plt.rcParams['ytick.color']        = '#cdd6f4'
plt.rcParams['text.color']         = '#cdd6f4'
plt.rcParams['grid.color']         = '#44475a'
plt.rcParams['grid.alpha']         = 0.5
plt.rcParams['legend.facecolor']   = '#313244'
plt.rcParams['legend.edgecolor']   = '#555577'


def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def measure_time(sort_func, arr, repeats=5):
    times = []
    for _ in range(repeats):
        data = arr.copy()
        start = time.perf_counter()
        sort_func(data)
        times.append(time.perf_counter() - start)
    return sum(times) / len(times)


print("=" * 60)
print("ЗАДАНИЕ 3: Эксперимент с пузырьковой сортировкой")
print("=" * 60)

sizes = [100, 200, 400, 800, 1600, 3200]
times_ms = []

for n in sizes:
    arr = [random.randint(0, 10_000) for _ in range(n)]
    t = measure_time(bubble_sort, arr, repeats=5)
    times_ms.append(t * 1000)
    print(f"  n={n:5d}  среднее время = {t * 1000:.4f} мс")

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Задание 3: Пузырьковая сортировка',
             fontsize=15, fontweight='bold', color='#cba6f7')

axes[0].plot(sizes, times_ms, 'o-', color='#f38ba8',
             linewidth=2.5, markersize=8, label='Bubble Sort')
axes[0].set_xlabel('Размер массива n')
axes[0].set_ylabel('Время (мс)')
axes[0].set_title('Зависимость времени от n')
axes[0].legend()
axes[0].grid(True)

n2_values = [n ** 2 for n in sizes]
axes[1].plot(n2_values, times_ms, 'o-', color='#a6e3a1',
             linewidth=2.5, markersize=8, label='Bubble Sort')
axes[1].set_xlabel('n²')
axes[1].set_ylabel('Время (мс)')
axes[1].set_title('Зависимость времени от n²\n(должна быть близка к прямой)')
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.savefig('task3_bubble.png', dpi=150, bbox_inches='tight')
plt.show()

print("\n  [OK] График сохранён: task3_bubble.png")
print("\nВывод: график t(n²) — прямая линия → поведение соответствует O(n²)")
