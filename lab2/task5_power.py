import time

# Задание 5/6: Возведение в степень
# Способ 1: Обычный циклический подход (последовательное умножение)
def power_loop(base, exp):
    if exp < 0:
        base = 1 / base
        exp = -exp
        
    result = 1
    for _ in range(exp):
        result *= base
    return result

# Способ 2: Быстрое возведение в степень (Рекурсия, Разделяй и властвуй)
def power_recursive_fast(base, exp):
    # Терминальная часть
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power_recursive_fast(base, -exp)
    
    # Рекурсивная часть (Деление пополам O(log N))
    half_power = power_recursive_fast(base, exp // 2)
    
    # Если степень четная: (x^(n/2))^2
    if exp % 2 == 0:
        return half_power * half_power
    # Если степень нечетная: x * (x^(n/2))^2
    else:
        return base * half_power * half_power

if __name__ == "__main__":
    bases = [2, 3, 1.01]
    expos = [10, 100, 500, 1000, 5000]
    
    print("=== Сравнение алгоритмов возведения в степень ===")
    for b in bases:
        for e in expos:
            # Измерение цикла
            start = time.perf_counter()
            res_loop = power_loop(b, e)
            loop_time = time.perf_counter() - start
            
            # Измерение быстрой рекурсии
            start = time.perf_counter()
            res_rec = power_recursive_fast(b, e)
            rec_time = time.perf_counter() - start
            
            print(f"{b}^{e}: Цикл = {loop_time:.7f} с, Рекурсия (быстрая) = {rec_time:.7f} с")
