def dfs(graph,start,visited=None):
    if visited is None:
        visited=set()
    visited.add(start)

    print(start)

    for next in graph[start]- visited:
        dfs(graph,next,visited)
    return visited
graph={"A":set(['B','D']),
       'B':set(['C','F']),
       'C':set(['E','G','H']),
       'G':set(['E','H']),
       'E':set(['B','F']),
       'F':set(['A']),
       'D':set(['F']),
       'H':set(['A']),
       }
dfs(graph,'A')