# Способ 1: Использование цикла
def count_spaces_loop(text: str) -> int:
    spaces_count = 0
    for char in text:
        if char == ' ':
            spaces_count += 1
    return spaces_count

# Способ 2: Использование рекурсии
def count_spaces_recursive(text: str) -> int:
    # 1. Терминальная часть: если строка пустая, пробелов нет (база рекурсии)
    if not text:
        return 0
    
    # 2. Рекурсивная часть:
    # Проверяем первый символ. Если он пробел, добавляем 1, иначе 0.
    # Затем прибавляем результат вызова функции для остатка строки text[1:]
    is_space = 1 if text[0] == ' ' else 0
    return is_space + count_spaces_recursive(text[1:])

if __name__ == "__main__":
    test_text = "Пример текста для проверки, здесь   несколько  пробелов."
    
    print(f"Текст: '{test_text}'")
    print(f"Пробелов (цикл): {count_spaces_loop(test_text)}")
    print(f"Пробелов (рекурсия): {count_spaces_recursive(test_text)}")
    
    # Для чтения из файла, если бы он был (имитация)
    # with open('text.txt', 'r', encoding='utf-8') as f:
    #     content = f.read()
    #     print(count_spaces_recursive(content))
