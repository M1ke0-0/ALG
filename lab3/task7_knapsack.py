import ast

def solve_knapsack():
    with open('treasures.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    list_str = content[content.find('['):]
    items = ast.literal_eval(list_str)
    
    C1, C2, C3 = 10, 14, 18
    n = len(items)
    
    dp = [ [[ [-1] * (C3 + 1) for _ in range(C2 + 1)] for __ in range(C1 + 1)] for ___ in range(n + 1) ]
    dp[0][0][0][0] = 0
    
    for i in range(1, n + 1):
        name, weight, val = items[i-1]
        
        for w1 in range(C1 + 1):
            for w2 in range(C2 + 1):
                for w3 in range(C3 + 1):
                    best_val = dp[i-1][w1][w2][w3]
                    
                    if w1 >= weight and dp[i-1][w1-weight][w2][w3] != -1:
                        best_val = max(best_val, dp[i-1][w1-weight][w2][w3] + val)
                        
                    if w2 >= weight and dp[i-1][w1][w2-weight][w3] != -1:
                        best_val = max(best_val, dp[i-1][w1][w2-weight][w3] + val)
                        
                    if w3 >= weight and dp[i-1][w1][w2][w3-weight] != -1:
                        best_val = max(best_val, dp[i-1][w1][w2][w3-weight] + val)
                        
                    dp[i][w1][w2][w3] = best_val

    max_val = -1
    best_state = (0, 0, 0)
    for w1 in range(C1 + 1):
        for w2 in range(C2 + 1):
            for w3 in range(C3 + 1):
                if dp[n][w1][w2][w3] > max_val:
                    max_val = dp[n][w1][w2][w3]
                    best_state = (w1, w2, w3)
                    
    print(f"Максимальная стоимость: {max_val}")
    
    w1, w2, w3 = best_state
    pack1, pack2, pack3 = [], [], []
    
    for i in range(n, 0, -1):
        name, weight, val = items[i-1]
        
        if dp[i][w1][w2][w3] == dp[i-1][w1][w2][w3]:
            pass
        elif w1 >= weight and dp[i-1][w1-weight][w2][w3] != -1 and dp[i][w1][w2][w3] == dp[i-1][w1-weight][w2][w3] + val:
            pack1.append(name)
            w1 -= weight
        elif w2 >= weight and dp[i-1][w1][w2-weight][w3] != -1 and dp[i][w1][w2][w3] == dp[i-1][w1][w2-weight][w3] + val:
            pack2.append(name)
            w2 -= weight
        elif w3 >= weight and dp[i-1][w1][w2][w3-weight] != -1 and dp[i][w1][w2][w3] == dp[i-1][w1][w2][w3-weight] + val:
            pack3.append(name)
            w3 -= weight

    print(f"Рюкзак Пети (10): {pack1[::-1]}")
    print(f"Рюкзак Васи (14): {pack2[::-1]}")
    print(f"Рюкзак Терентия (18): {pack3[::-1]}")

if __name__ == "__main__":
    solve_knapsack()
