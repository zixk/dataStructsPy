def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        print(next)
        dfs(graph, next, visited)
    return visited


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
    print(dfs(graph, "A"))