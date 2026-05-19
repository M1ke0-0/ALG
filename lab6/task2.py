import sys

# Настройка кодировки для корректного вывода кириллицы на Windows
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except AttributeError:
    pass

class Node:
    """Узел односвязного списка, содержащий данные и ссылку на следующий узел."""
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class SinglyLinkedList:
    """Односвязный список, хранящий только указатель head."""
    def __init__(self):
        self.head = None
        self._size = 0

    def get_size(self):
        """Возвращает количество элементов в списке."""
        return self._size

    def add_to_front(self, value):
        """Добавление значения в начало списка (O(1))."""
        new_node = Node(value, self.head)
        self.head = new_node
        self._size += 1

    def add_to_back(self, value):
        """Добавление значения в конец списка (O(N) без tail)."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next_node is not None:
                curr = curr.next_node
            curr.next_node = new_node
        self._size += 1

    def remove_first(self):
        """Удаление первого элемента (O(1))."""
        if self.head is None:
            raise IndexError("Попытка удаления из пустого списка")
        
        removed_value = self.head.value
        self.head = self.head.next_node
        self._size -= 1
        return removed_value

    def remove_last(self):
        """Удаление последнего элемента (O(N) без tail)."""
        if self.head is None:
            raise IndexError("Попытка удаления из пустого списка")
        
        if self.head.next_node is None:
            # Если в списке всего один элемент
            removed_value = self.head.value
            self.head = None
            self._size -= 1
            return removed_value

        # Проход до предпоследнего узла
        curr = self.head
        while curr.next_node.next_node is not None:
            curr = curr.next_node
        
        removed_value = curr.next_node.value
        curr.next_node = None
        self._size -= 1
        return removed_value

    def get(self, index):
        """Получение значения по индексу (O(N))."""
        if not 0 <= index < self._size:
            raise IndexError("Индекс вышел за пределы диапазона")
        
        curr = self.head
        for _ in range(index):
            curr = curr.next_node
        return curr.value

    def to_list(self):
        """Преобразование списка в стандартный Python-список для удобного вывода."""
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.value)
            curr = curr.next_node
        return result

    def __str__(self):
        # Красивое текстовое представление списка
        if self.head is None:
            return "Пустой список"
        nodes = []
        curr = self.head
        while curr is not None:
            nodes.append(str(curr.value))
            curr = curr.next_node
        return " -> ".join(nodes)


if __name__ == "__main__":
    print("=== ЗАДАНИЕ 2. ТЕСТИРОВАНИЕ ОДНОСВЯЗНОГО СПИСКА ===")

    # 1. Создать список
    ll = SinglyLinkedList()
    print(f"Создан пустой список: {ll}, размер: {ll.get_size()}")

    # 2. Последовательно добавить в него значения 5, 3, 5, 20
    print("\nПоследовательное добавление значений 5, 3, 5, 20 (в конец списка):")
    for val in [5, 3, 5, 20]:
        ll.add_to_back(val)
        print(f"Добавлен {val}: {ll}, размер: {ll.get_size()}")

    # 3. Добавить значение 7 в конец списка
    print("\nДобавление значения 7 в конец списка:")
    ll.add_to_back(7)
    print(f"Результат: {ll}, размер: {ll.get_size()}")

    # 4. Удалить первый элемент
    print("\nУдаление первого элемента:")
    first = ll.remove_first()
    print(f"Удален первый элемент ({first}). Результат: {ll}, размер: {ll.get_size()}")

    # 5. Удалить последний элемент
    print("\nУдаление последнего элемента:")
    last = ll.remove_last()
    print(f"Удален последний элемент ({last}). Результат: {ll}, размер: {ll.get_size()}")

    # 6. Вывести итоговую последовательность
    print(f"\nИтоговая последовательность: {ll}")
    print(f"Итоговый размер: {ll.get_size()}")

    # Дополнительно продемонстрируем получение значения по индексу
    if ll.get_size() > 0:
        idx = 1
        print(f"Значение по индексу {idx}: {ll.get(idx)}")

    # --- ТЕОРЕТИЧЕСКИЕ ОБЪЯСНЕНИЯ ---
    explanation = """
=== ОТВЕТЫ И ВЫВОДЫ ПО ЗАДАНИЮ 2 ===

1. В чём состоят преимущества и недостатки односвязного списка по сравнению с массивом?
   Преимущества:
   - Динамический размер: память выделяется узлами по мере необходимости, нет затрат на операции resize.
   - Эффективная вставка и удаление в начале списка: выполняются за O(1), так как не требуют сдвига элементов.
   - Отсутствие необходимости в непрерывном блоке памяти: узлы могут находиться в любых свободных адресах памяти.
   Недостатки:
   - Медленный доступ по индексу: получение элемента по индексу требует последовательного обхода с начала списка (O(N)).
   - Дополнительные затраты памяти: каждый узел хранит не только полезные данные, но и ссылку на следующий узел (указатель).
   - Вставка и удаление в конце или в середине требуют времени O(N), если нет прямой ссылки на предшествующий узел.

2. Почему добавление и удаление в начале списка выполняются просто, а получение по индексу требует прохода по узлам?
   - В начале списка: мы всегда имеем прямой указатель head на первый узел. Чтобы добавить элемент в начало, 
     достаточно связать новый узел с текущим head и обновить head на новый узел (O(1)). Чтобы удалить первый 
     элемент, достаточно перенаправить head на head.next_node (O(1)).
   - Получение по индексу: узлы не лежат в памяти друг за другом, поэтому мы не можем вычислить адрес по формуле. 
     Единственный способ найти k-й элемент — начать с head и последовательно перейти по ссылкам "next" k раз (O(N)).

3. Какую роль играет указатель head?
   Указатель head — это "входные ворота" в связанный список. Поскольку узлы распределены в памяти хаотично, 
   head хранит адрес первого узла, с которого начинается любая операция (поиск, добавление, удаление). 
   Если мы потеряем указатель head (например, случайно присвоим ему None), мы потеряем доступ ко всему списку, 
   и сборщик мусора удалит всю цепочку узлов из памяти.
"""
    print(explanation)
