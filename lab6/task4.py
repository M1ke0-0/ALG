import sys
import time
import random
import matplotlib.pyplot as plt

# Настройка кодировки для корректного вывода кириллицы на Windows
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except AttributeError:
    pass

# Импортируем наши структуры данных из предыдущих заданий
from task1 import DynamicArray
from task2 import SinglyLinkedList

def run_benchmark():
    sizes = [100, 1000, 10000]
    M = 1000  # Количество повторений операций для замера времени

    # Словари для хранения результатов
    # Формат: {размер_N: {операция: время}}
    array_results = {}
    list_results = {}

    print(f"Запуск вычислительного исследования (M = {M} операций на замер)...")

    for N in sizes:
        print(f"\nТестирование для N = {N}...")

        # --- 1. ТЕСТИРОВАНИЕ ДИНАМИЧЕСКОГО МАССИВА ---
        # Подготовка структуры
        arr = DynamicArray()
        for i in range(N):
            arr.append(i)

        # А. Добавление в конец
        # Чтобы не раздувать структуру бесконечно, замерим добавление M элементов
        t0 = time.perf_counter()
        for i in range(M):
            arr.append(999)
        t_arr_append = time.perf_counter() - t0

        # Б. Удаление из начала
        # Удаляем M элементов из начала
        t0 = time.perf_counter()
        for _ in range(M):
            arr.remove_at(0)
        t_arr_remove = time.perf_counter() - t0

        # В. Получение элемента по индексу
        # Генерируем случайные индексы для честности теста
        indices = [random.randint(0, arr.get_size() - 1) for _ in range(M)]
        t0 = time.perf_counter()
        for idx in indices:
            _ = arr.get(idx)
        t_arr_get = time.perf_counter() - t0

        # Г. Получение размера структуры
        t0 = time.perf_counter()
        for _ in range(M):
            _ = arr.get_size()
        t_arr_size = time.perf_counter() - t0

        array_results[N] = {
            'append': t_arr_append,
            'remove_first': t_arr_remove,
            'get': t_arr_get,
            'size': t_arr_size
        }

        # --- 2. ТЕСТИРОВАНИЕ ОДНОСВЯЗНОГО СПИСКА ---
        # Подготовка структуры
        ll = SinglyLinkedList()
        # Оптимизированное заполнение списка за O(N) вместо O(N^2)
        # Вставляем элементы с конца в начало, получая в итоге 0 -> 1 -> ... -> N-1
        for i in range(N - 1, -1, -1):
            ll.add_to_front(i)

        # А. Добавление в конец (O(N) без tail)
        t0 = time.perf_counter()
        for i in range(M):
            ll.add_to_back(999)
        t_list_append = time.perf_counter() - t0

        # Б. Удаление из начала (O(1))
        t0 = time.perf_counter()
        for _ in range(M):
            ll.remove_first()
        t_list_remove = time.perf_counter() - t0

        # В. Получение элемента по индексу (O(N))
        indices = [random.randint(0, ll.get_size() - 1) for _ in range(M)]
        t0 = time.perf_counter()
        for idx in indices:
            _ = ll.get(idx)
        t_list_get = time.perf_counter() - t0

        # Г. Получение размера структуры (O(1))
        t0 = time.perf_counter()
        for _ in range(M):
            _ = ll.get_size()
        t_list_size = time.perf_counter() - t0

        list_results[N] = {
            'append': t_list_append,
            'remove_first': t_list_remove,
            'get': t_list_get,
            'size': t_list_size
        }

    # Вывод результатов в виде Markdown-таблицы
    print("\n" + "="*80)
    print(" РЕЗУЛЬТАТЫ СРАВНЕНИЯ (время выполнения в секундах)")
    print("="*80)
    print(f"| Размер (N) | Структура       | Добавление в конец | Удаление из начала | Получение по индексу | Получение размера |")
    print(f"|------------|-----------------|---------------------|---------------------|----------------------|-------------------|")
    for N in sizes:
        a = array_results[N]
        l = list_results[N]
        print(f"| {N:<10} | Динам. массив   | {a['append']:19.6f} | {a['remove_first']:19.6f} | {a['get']:20.6f} | {a['size']:17.6f} |")
        print(f"|            | Связанный список| {l['append']:19.6f} | {l['remove_first']:19.6f} | {l['get']:20.6f} | {l['size']:17.6f} |")
        print(f"|------------|-----------------|---------------------|---------------------|----------------------|-------------------|")

    # Построение графиков
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Сравнение производительности: Динамический массив vs Односвязный список", fontsize=16, fontweight='bold', color='#2C3E50')

    operations = [
        ('append', 'Добавление в конец', axs[0, 0]),
        ('remove_first', 'Удаление из начала', axs[0, 1]),
        ('get', 'Получение по индексу', axs[1, 0]),
        ('size', 'Получение размера', axs[1, 1])
    ]

    for key, title, ax in operations:
        arr_times = [array_results[N][key] for N in sizes]
        list_times = [list_results[N][key] for N in sizes]

        ax.plot(sizes, arr_times, 'o-', linewidth=2.5, color='#E67E22', label='Динамический массив')
        ax.plot(sizes, list_times, 's--', linewidth=2.5, color='#2980B9', label='Односвязный список')
        
        ax.set_title(title, fontsize=12, fontweight='semibold', color='#34495E')
        ax.set_xlabel('Размер структуры (N)', fontsize=10)
        ax.set_ylabel('Время (сек) для M=1000 опер.', fontsize=10)
        ax.set_xscale('log')
        if key in ['append', 'get', 'remove_first']:
            ax.set_yscale('log') # Логарифмический масштаб для наглядности при больших различиях
        ax.grid(True, which="both", ls="--", alpha=0.5)
        ax.legend(frameon=True, facecolor='white', edgecolor='none')

    plt.tight_layout()
    plot_filename = 'comparison_plot.png'
    plt.savefig(plot_filename, dpi=300)
    print(f"\nГрафик успешно сохранен как '{plot_filename}'")

    # --- ТЕОРЕТИЧЕСКИЕ ОБЪЯСНЕНИЯ И ВЫВОДЫ ---
    conclusions = """
=== ОБЪЯСНЕНИЯ И ВЫВОДЫ ПО ЗАДАНИЮ 4 ===

1. Почему массивы особенно удобны для индексного доступа?
   Массив выделяет непрерывный блок памяти. Это позволяет осуществлять произвольный доступ (random access) 
   к любому элементу по формуле смещения за константное время O(1), независимо от положения элемента в массиве. 
   Процессору достаточно знать адрес начала массива и индекс элемента. 
   Связанный же список вынужден последовательно переходить по указателям узлов от головы списка (head) 
   до нужного индекса, что приводит к линейной сложности O(N).

2. Почему связанные списки особенно удобны для вставки и удаления без сдвига элементов?
   В связанном списке элементы логически связаны ссылками, но физически могут быть разбросаны по памяти. 
   При удалении или добавлении элемента в начало связанного списка нам не нужно перемещать или сдвигать другие данные — 
   достаточно создать новый узел и перенаправить указатели (ссылки). Это операция константной сложности O(1).
   В массиве же любая вставка или удаление в начале или середине требует физического сдвига всех последующих 
   элементов памяти, чтобы заполнить пустоту или освободить место, что требует O(N) операций.

3. ИТОГОВЫЙ ВЫВОД: когда что лучше использовать?
   - ДИНАМИЧЕСКИЙ МАССИВ (Python list, C++ vector) лучше использовать, когда:
     1. Основная операция в программе — это частое чтение или обновление данных по конкретным индексам.
     2. Добавление элементов происходит преимущественно в конец списка (амортизированное O(1)).
     3. Память должна расходоваться максимально эффективно без накладных расходов на хранение указателей.
   
   - СВЯЗАННЫЙ СПИСОК (Linked List) лучше использовать, когда:
     1. Требуется часто вставлять и удалять элементы в начало списка или в места, где у нас уже есть ссылка на узел (O(1)).
     2. Объем данных заранее абсолютно неизвестен и крайне динамичен, а выделение больших непрерывных кусков памяти затруднено.
     3. Не требуется произвольный доступ к элементам по индексам.
"""
    print(conclusions)


if __name__ == "__main__":
    run_benchmark()
