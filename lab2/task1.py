from decimal import Decimal
from fractions import Fraction

def calculate_order():
    prices = [19.99, 5.49, 3.50, 12.30, 49.64, 31.01, 7.99]
    
    # Способ 1: float
    total_float = sum(prices)
    discount_float = total_float * 0.07
    after_discount_float = total_float - discount_float
    vat_float = after_discount_float * 0.20
    final_total_float = after_discount_float + vat_float
    part_float = final_total_float / 3
    
    print("----- FLOAT -----")
    print(f"Итоговая сумма: {final_total_float}")
    print(f"Одна часть: {part_float}\n")
    
    # Способ 2: Decimal
    total_dec = sum(Decimal(str(p)) for p in prices)
    discount_dec = total_dec * Decimal('0.07')
    after_discount_dec = total_dec - discount_dec
    vat_dec = after_discount_dec * Decimal('0.20')
    final_total_dec = after_discount_dec + vat_dec
    part_dec = final_total_dec / Decimal(3)
    
    print("----- DECIMAL -----")
    print(f"Итоговая сумма: {final_total_dec}")
    print(f"Одна часть: {part_dec}\n")
    
    # Способ 3: Fraction
    total_frac = sum(Fraction(str(p)) for p in prices)
    discount_frac = total_frac * Fraction('7/100')
    after_discount_frac = total_frac - discount_frac
    vat_frac = after_discount_frac * Fraction('20/100')
    final_total_frac = after_discount_frac + vat_frac
    part_frac = final_total_frac / Fraction(3)
    
    print("----- FRACTION -----")
    print(f"Итоговая сумма (дробь): {final_total_frac}")
    print(f"Итоговая сумма (float): {float(final_total_frac)}")
    print(f"Одна часть (дробь): {part_frac}")
    print(f"Одна часть (float): {float(part_frac)}\n")

if __name__ == "__main__":
    calculate_order()
