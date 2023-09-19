from queue import Queue

def bfs(start, end, graph):
    n = len(graph)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    q = Queue()
    q.put((start[0], start[1], 0))
    visited.add((start[0], start[1], 0))
    while not q.empty():
        x, y, t = q.get()
        if (x, y) == (end[0], end[1]):
            return t
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if (nx, ny, (t+1)%3) in visited:
                continue
            if graph[nx][ny][(t+1)%3] == '1':
                continue
            visited.add((nx, ny, (t+1)%3))
            q.put((nx, ny, t+1))
    return -1
if __name__ == "__main__":
    n = 3# int(input())
    k = 1 #int(input())
    monster_pos = [(0,2),(0,0)]
    #for i in range(k):
    #    row, col = map(int, input().split())
    #    monster_pos.append((row, col))
    princess, prince = ([2,2],[0,0])#map(int, input().split())
    graph = \
    [
    ['000', '011' ,'000'],
    ['000', '000', '000'],
    ['000', '000', '000']
    ]
    #for i in range(n):
    #    row = input().split()
    #    graph.append(row)

    min_time = bfs(prince, princess, graph)

    print(min_time)
