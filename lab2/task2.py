import time
import sys

# Способ 1: Цикл
def factorial_loop(n):
    if n < 0:
        raise ValueError("Факториал определен только для положительных чисел (>= 0)")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Способ 2: Рекурсия
def factorial_recursive(n):
    if n < 0:
        raise ValueError("Факториал определен только для положительных чисел (>= 0)")
    # Терминальная часть: база рекурсии
    if n == 0 or n == 1:
        return 1
    # Рекурсивная часть
    return n * factorial_recursive(n - 1)

def measure_performance():
    values_to_test = [10, 50, 100, 500, 900]
    
    print("=== Сравнение производительности: ===")
    for n in values_to_test:
        # Измеряем цикл
        start_time = time.perf_counter()
        factorial_loop(n)
        loop_time = time.perf_counter() - start_time
        
        # Измеряем рекурсию
        start_time = time.perf_counter()
        factorial_recursive(n)
        rec_time = time.perf_counter() - start_time
        
        print(f"n = {n}: Цикл = {loop_time:.7f} с, Рекурсия = {rec_time:.7f} с")

    print("\nПробуем вычислить factorial_recursive(1000)...")
    try:
        factorial_recursive(1000)
    except Exception as e:
        print(f"Произошла ошибка: {type(e).__name__} - {e}")
        print("В Python по умолчанию максимальная глубина рекурсии равна 1000 (sys.getrecursionlimit() = {})".format(sys.getrecursionlimit()))

if __name__ == "__main__":
    measure_performance()
