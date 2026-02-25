import math

print("ЗАДАНИЕ 5: Оценка времени масштабирования O(n log n)")print("=" * 60)

n1 = 1_000_000
t1 = 120
n2 = 4_000_000

# Формула:
#   T(n) = C · n · log₂(n)
#   T2/T1 = (n2 · log₂(n2)) / (n1 · log₂(n1))

log_n1 = math.log2(n1)
log_n2 = math.log2(n2)
ratio  = (n2 * log_n2) / (n1 * log_n1)
t2     = t1 * ratio

print(f"\n  n1 = {n1:>12,}    T1 = {t1} мс")
print(f"  n2 = {n2:>12,}")
print()
print("  Формула:")
print("    T2/T1 = (n2 · log₂(n2)) / (n1 · log₂(n1))")
print(f"          = ({n2:,} · {log_n2:.4f}) / ({n1:,} · {log_n1:.4f})")
print(f"          = {n2 * log_n2:,.2f} / {n1 * log_n1:,.2f}")
print(f"          = {ratio:.6f}")
print()
print(f"  T2 = T1 · {ratio:.4f}")
print(f"     = {t1} · {ratio:.4f}")
print(f"     ≈ {t2:.2f} мс  ({t2 / 1000:.3f} с)")
print()
print("  Для сравнения (если бы алгоритм был O(n²)):")
ratio_n2 = (n2 / n1) ** 2
print(f"    T2_square = {t1} · ({n2/n1})² = {t1} · {ratio_n2:.0f} = {t1 * ratio_n2:.0f} мс")
print()
print(f"  Ответ: T(n2) ≈ {t2:.1f} мс ≈ {t2 / 1000:.3f} с")
