amounts = [23, 37, 58, 74, 99, 123]
coins1 = [1, 5, 10, 25, 50, 100]
coins2 = [1, 4, 6, 9]

def greedy_change(amount, coins):
    coins = sorted(coins, reverse=True)
    res = []
    for c in coins:
        while amount >= c:
            res.append(c)
            amount -= c
    return res

def dp_change(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    parent = [-1] * (amount + 1)
    
    for i in range(1, amount + 1):
        for c in coins:
            if i >= c and dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1
                parent[i] = c
                
    if dp[amount] == float('inf'):
        return None
        
    res = []
    curr = amount
    while curr > 0:
        res.append(parent[curr])
        curr -= parent[curr]
    return res

def run():
    for coins in [coins1, coins2]:
        print(f"\nНабор номиналов: {coins}")
        for amount in amounts:
            greedy_res = greedy_change(amount, coins)
            dp_res = dp_change(amount, coins)
            
            greedy_count = len(greedy_res)
            dp_count = len(dp_res)
            
            match = "Да" if greedy_count == dp_count else "Нет"
            
            print(f"Сумма: {amount} | Жадный: {greedy_count} шт {greedy_res} | ДП: {dp_count} шт {dp_res} | Совпали: {match}")

if __name__ == "__main__":
    run()
