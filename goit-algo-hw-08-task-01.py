import heapq

def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)
    
    total_cost = 0
    
    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        cost = first + second
        total_cost += cost
        
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад
cables = [4, 3, 2, 6]
print(f"Мінімальна сума загальних витрат: {min_cost_to_connect_cables(cables)}")

