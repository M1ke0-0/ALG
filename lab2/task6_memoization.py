import random
import time

# --- Задание 6.1 Декоратор ---
def memoize(func):
    """Декоратор для кэширования результатов функции."""
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

# Демонстрация мемоизации: Вычисление чисел Фибоначчи
@memoize
def fib_memo(n):
    if n < 2:
        return n
    return fib_memo(n-1) + fib_memo(n-2)

def fib_no_memo(n):
    if n < 2:
        return n
    return fib_no_memo(n-1) + fib_no_memo(n-2)

# --- Задание 6.2 Число путей в прямоугольной сетке ---
@memoize
def count_paths(m, n):
    """
    Рекурсивная функция подсчета путей в сетке m x n.
    Двигаться можно только вправо и вниз.
    """
    # Базовый случай: если сетка 1xN или Mx1, то путь только один (по прямой)
    if m == 1 or n == 1:
        return 1
    # Рекурсивный случай: шаг вниз (m-1) + шаг вправо (n-1)
    return count_paths(m - 1, n) + count_paths(m, n - 1)

# --- Задание 6.3 Умножение на случайную величину ---
def multiply_by_random(n, times=1):
    """
    Рекурсивно умножает число n на случайный коэффициент times раз.
    (Добавил параметр times для смысла рекурсии, 
    иначе умножение на случайную величину 1 раз не требует рекурсии)
    """
    if times == 0:
        return n
    
    coef = random.uniform(0.5, 2.0) # Случайный коэффициент от 0.5 до 2.0
    return multiply_by_random(n * coef, times - 1)

# --- Задание 6.4 Проверка числа на простоту ---
def is_prime(n, divisor=None):
    """Рекурсивная проверка числа на простоту."""
    # Обработка базовых случаев
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    # Инициализация первого делителя
    if divisor is None:
        divisor = int(n**0.5)
        
    # Терминальная часть: если перебрали все до 1, число простое
    if divisor == 1:
        return True
        
    # Если нашли делитель без остатка — число составное
    if n % divisor == 0:
        return False
        
    # Рекурсивный вызов для следующего меньшего делителя
    return is_prime(n, divisor - 1)


if __name__ == "__main__":
    print("--- 6.1 Демонстрация мемоизации (Fibonacci) ---")
    start = time.perf_counter()
    fib_no_memo(35) # без мемоизации это долго
    print(f"Без memoize(35): {time.perf_counter() - start:.4f} сек")
    
    start = time.perf_counter()
    fib_memo(35)
    print(f"C memoize(35)  : {time.perf_counter() - start:.4f} сек")

    print("\n--- 6.2 Число путей в прямоугольной сетке ---")
    print(f"Сетка 3x3: {count_paths(3, 3)} путей")
    print(f"Сетка 10x10: {count_paths(10, 10)} путей")
    
    print("\n--- 6.3 Умножение на случайную величину ---")
    val = 100
    print(f"Начальное: {val}, После 3-х случайных умножений: {multiply_by_random(val, 3):.2f}")
    
    print("\n--- 6.4 Проверка на простоту ---")
    for num in [17, 20, 97, 100, 997]:
        print(f"Число {num} простое? {is_prime(num)}")
