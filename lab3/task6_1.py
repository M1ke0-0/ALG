stations = [120, 260, 410, 560, 730, 890, 1040, 1190, 1360, 1520, 1680, 1840, 2010, 2170, 2330, 2480, 2650, 2810, 2970, 3140, 3300, 3460, 3630, 3790, 3950, 4120, 4280, 4440, 4610, 4770, 4930, 5100, 5260, 5420, 5590, 5750, 5910, 6080, 6240, 6400, 6570, 6730, 6890, 7060, 7220, 7380, 7550, 7710, 7870, 8040, 8200, 8360, 8530, 8690, 8850, 9020, 9180, 9340, 9510, 9670, 9830, 10000, 10160, 10320]

def min_stops_to_vladivostok(distance, capacity, stations):
    stops = []
    current_pos = 0
    n = len(stations)
    
    while current_pos + capacity < distance:
        next_station = -1
        for i in range(n):
            if stations[i] <= current_pos + capacity and stations[i] > current_pos:
                next_station = stations[i]
                
        if next_station == -1:
            print("Невозможно доехать!")
            return None
            
        stops.append(next_station)
        current_pos = next_station
        
    return stops

def solve():
    dist = 10451
    cap = 500
    stops = min_stops_to_vladivostok(dist, cap, stations)
    if stops is not None:
        print(f"Количество остановок: {len(stops)}")
        print(f"Остановки: {stops[:5]} ... {stops[-5:]}")

if __name__ == "__main__":
    solve()
