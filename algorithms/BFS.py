
def bfs(graph, start):
    visited = set()
    Q = [start]
    while(Q):
        vertex = Q.pop(0)
        if(vertex not in visited):
            print(vertex)
            visited.add(vertex)
            Q.extend(graph[vertex] - visited)


if __name__ == "__main__":
    graph = {"A": set(["B", "C", "D", "E"]),
             "B": set(["A","F","G"]),
             "C": set(["A", "H", "I"]),
             "D": set(["A", "J", "K", "L"]),
             "E": set(["A", "M"]),
             "F": set(["B"]),
             "G": set(["B"]),
             "H": set(["C"]),
             "I": set(["C"]),
             "J": set(["D"]),
             "K": set(["D"]),
             "L": set(["D"]),
             "M": set(["E"]),  
            }
    print(bfs(graph, "A"))
