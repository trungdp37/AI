import random

# Khởi tạo 1 chuỗi thành phố mặc định 
def randomSolution(tsp):
    cities = list(range(len(tsp)))
    solution = []

    for i in range(len(tsp)):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)

    return solution

# Lấy tổng giá trị đường đi
def routeLength(tsp, solution):
    routeLength = 0
    for i in range(len(solution)):
        routeLength += tsp[solution[i-1]][solution[i]]

    return routeLength

# Khởi tạo các đường đi khác từ đường đi mặc định có sẵn
# Swap từng cặp đỉnh từ đường đi mặc định để cho ra đường đi mới  
def getNeighbors(solution):
    neighbors = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbor = solution.copy()
            neighbor[i] = neighbor[j]
            neighbor[j] = solution[i]
            neighbors.append(neighbor)
    return neighbors

# Tính toán đường đi tối ưu nhất
def getBestNeighbor(tsp, neighbors):
    bestRouteLength = routeLength(tsp, neighbors[0])
    bestNeighbor = neighbors[0]
    for neighbor in neighbors:
        currRouteLength = routeLength(tsp, neighbor)
        if currRouteLength < bestRouteLength:
            bestRouteLength = currRouteLength
            bestNeighbor = neighbor
    return bestNeighbor, bestRouteLength

# Thực hiện thuật toán
def hillclimbing(tsp):
    currSolution = randomSolution(tsp)
    currRouteLength = routeLength(tsp, currSolution)
    neighbors = getNeighbors(currSolution)
    bestNeighbor, bestNeighborRouteLength = getBestNeighbor(tsp, neighbors)

    while bestNeighborRouteLength < currRouteLength:
        currSolution = bestNeighbor
        currRouteLength = bestNeighborRouteLength
        neighbors = getNeighbors(currSolution)
        bestNeighbor, bestNeighborRouteLength = getBestNeighbor(tsp, neighbors)
    
    return currSolution, currRouteLength

def main():
    tsp = [[0, 4, 5, 3],
           [4, 0, 3, 5],
           [5, 3, 0, 4],
           [3, 5, 4, 0],
           ]
    print(hillclimbing(tsp))

if __name__ == "__main__":
    main()