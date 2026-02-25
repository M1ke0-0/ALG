print("ЗАДАНИЕ 2: Работа с нотациями  O / Ω / Θ")

functions = [
    {
        "expr":  "t(n) = 3n² + 7n + 5",
        "O":     "O(n²)",
        "Omega": "Ω(n²)",
        "Theta": "Θ(n²)",
        "note":  "Доминирует n², члены 7n и 5 пренебрежимы при n→∞",
    },
    {
        "expr":  "t(n) = 5n·log n + 20n",
        "O":     "O(n log n)",
        "Omega": "Ω(n log n)",
        "Theta": "Θ(n log n)",
        "note":  "n·log n растёт быстрее n; 5n·log n+20n ≤ 25·n·log n",
    },
    {
        "expr":  "t(n) = 100",
        "O":     "O(1)",
        "Omega": "Ω(1)",
        "Theta": "Θ(1)",
        "note":  "Константа, не зависит от n",
    },
    {
        "expr":  "t(n) = 2ⁿ + n³",
        "O":     "O(2ⁿ)",
        "Omega": "Ω(2ⁿ)",
        "Theta": "Θ(2ⁿ)",
        "note":  "2ⁿ >> n³ при n≥10; экспонента доминирует",
    },
]

header = f"{'Функция':<25} {'O (верхн.)':<14} {'Ω (нижн.)':<14} {'Θ (точная)':<14}"
print("\n" + header)
print("-" * 67)
for f in functions:
    print(f"  {f['expr']:<23} {f['O']:<14} {f['Omega']:<14} {f['Theta']:<14}")

print()
print("Обоснования:")
for i, f in enumerate(functions, 1):
    print(f"  {i}. {f['expr']}")
    print(f"     → {f['note']}")
    print(f"     → {f['Theta']}\n")
