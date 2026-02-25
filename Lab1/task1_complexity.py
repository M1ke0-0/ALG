n = 16

print("=" * 55)
print("ЗАДАНИЕ 1: Классификация сложности")
print("=" * 55)
print(f"\n[Цикл 1] O(n) — линейная сложность  (n={n})")
count = 0
for i in range(n):
    count += 1
print(f"  Итераций: {count}  (ожидается n = {n})")

print(f"\n[Цикл 2] O(n²) — квадратичная сложность  (n={n})")
count = 0
for i in range(n):
    for j in range(n):
        count += 1
print(f"  Итераций: {count}  (ожидается n² = {n**2})")


print(f"\n[Цикл 3] O(log n) — логарифмическая сложность  (n={n})")
count = 0
i = 1
while i < n:
    i *= 2
    count += 1
import math
print(f"  Итераций: {count}  (ожидается ⌈log₂(n)⌉ = {math.ceil(math.log2(n))})")

print(f"\n[Цикл 4] O(n²) — треугольная итерация  (n={n})")
count = 0
for i in range(n):
    for j in range(i):
        count += 1
print(f"  Итераций: {count}  (ожидается n(n-1)/2 = {n*(n-1)//2})")

print("\n" + "=" * 55)
print("Сводка асимптотических оценок:")
print("  Цикл 1: O(n)")
print("  Цикл 2: O(n²)")
print("  Цикл 3: O(log n)")
print("  Цикл 4: O(n²)")
