"""
Лабораторная работа 2 — Задание 1
Числовые типы Python: float, Decimal, Fraction
Расчёт стоимости заказа интернет-магазина
"""

from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction

prices = [19.99, 5.49, 3.50, 12.30, 49.64, 31.01, 7.99]

DISCOUNT = 0.07   # скидка 7%
VAT      = 0.20   # НДС 20%
PARTS    = 3      # на 3 равные части


def calc_float(prices):
    """Расчёт с использованием float."""
    total = sum(prices)
    after_discount = total * (1 - DISCOUNT)
    after_vat = after_discount * (1 + VAT)
    one_part = after_vat / PARTS
    return total, after_vat, one_part


def calc_decimal(prices):
    """Расчёт с использованием Decimal."""
    discount = Decimal(str(DISCOUNT))
    vat      = Decimal(str(VAT))
    parts    = Decimal(str(PARTS))

    total = sum(Decimal(str(p)) for p in prices)
    after_discount = total * (1 - discount)
    after_vat = after_discount * (1 + vat)
    one_part = after_vat / parts
    return total, after_vat, one_part


def calc_fraction(prices):
    """Расчёт с использованием Fraction."""
    discount = Fraction(7, 100)    # 7%
    vat      = Fraction(20, 100)   # 20%
    parts    = Fraction(3)

    # Конвертируем float-цены через строку, чтобы избежать накопленной ошибки
    total = sum(Fraction(str(p)) for p in prices)
    after_discount = total * (1 - discount)
    after_vat = after_discount * (1 + vat)
    one_part = after_vat / parts
    return total, after_vat, one_part


# ─── float ────────────────────────────────────────────────────────────────────
total_f, final_f, part_f = calc_float(prices)
print("=" * 55)
print("  float")
print("=" * 55)
print(f"  Сумма заказа    : {total_f:.10f}")
print(f"  Итоговая сумма  : {final_f:.10f}")
print(f"  Одна часть (1/3): {part_f:.10f}")

# ─── Decimal ──────────────────────────────────────────────────────────────────
total_d, final_d, part_d = calc_decimal(prices)
print()
print("=" * 55)
print("  Decimal")
print("=" * 55)
print(f"  Сумма заказа    : {total_d}")
print(f"  Итоговая сумма  : {final_d}")
print(f"  Одна часть (1/3): {part_d}")
# Округлённое банковское значение до 2 знаков
part_d_rounded = part_d.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print(f"  Одна часть (округл.): {part_d_rounded}")

# ─── Fraction ─────────────────────────────────────────────────────────────────
total_fr, final_fr, part_fr = calc_fraction(prices)
print()
print("=" * 55)
print("  Fraction")
print("=" * 55)
print(f"  Сумма заказа    : {total_fr}  ~=  {float(total_fr):.10f}")
print(f"  Итоговая сумма  : {final_fr}  ~=  {float(final_fr):.10f}")
print(f"  Одна часть (1/3): {part_fr}  ~=  {float(part_fr):.10f}")

# ─── Сравнение ────────────────────────────────────────────────────────────────
print()
print("=" * 55)
print("  Сравнение итоговых значений (одна часть)")
print("=" * 55)
print(f"  float    : {part_f:.10f}")
print(f"  Decimal  : {float(part_d):.10f}")
print(f"  Fraction : {float(part_fr):.10f}")

diff_f_d  = abs(part_f - float(part_d))
diff_f_fr = abs(part_f - float(part_fr))
print(f"\n  Разность float <-> Decimal  : {diff_f_d:.2e}")
print(f"  Разность float <-> Fraction : {diff_f_fr:.2e}")

print("""
─── Вывод ────────────────────────────────────────────────────────
  • float  — хранит числа в двоичном формате IEEE 754. При операциях
    с дробными числами накапливается погрешность округления.
  • Decimal — хранит числа в десятичном формате с настраиваемой
    точностью. Даёт точно предсказуемый результат для финансов.
  • Fraction — представляет числа как дроби (числитель / знаменатель),
    обеспечивая математически точный результат, но медленнее
    и даёт периодические дроби при делении на 3.
  Для финансовых расчётов рекомендуется Decimal: он точен,
  поддерживает банковское округление и работает быстро.
──────────────────────────────────────────────────────────────────
""")
