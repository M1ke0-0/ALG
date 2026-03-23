import ast

def solve_task5():
    with open('works.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    list_str = content[content.find('['):]
    events = ast.literal_eval(list_str)
    
    days_order = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5}
    
    events.sort(key=lambda x: (days_order[x[1]], x[3][0], x[3][1]))
    
    selected_events = []
    last_end_time = {day: (0, 0) for day in days_order.keys()}
    
    for event in events:
        title, day, start, end, desc = event
        
        if start >= last_end_time[day]:
            selected_events.append(event)
            last_end_time[day] = end
            
    print(f"Выбрано мероприятий: {len(selected_events)}")
    for e in selected_events[:10]:
        print(f"{e[1]} {e[2][0]:02d}:{e[2][1]:02d}-{e[3][0]:02d}:{e[3][1]:02d} | {e[0]} ({e[4]})")
    print("...")

if __name__ == "__main__":
    solve_task5()
