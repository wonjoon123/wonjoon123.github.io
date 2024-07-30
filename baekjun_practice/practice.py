n = int(input())
how_many= int(input())

graph = {i:[] for i in range(1,n+1)}


for _ in range(how_many):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)



def bfs(graph:dict, start = 1):
    stack = 0
    visited = {i: False for i in range(1,n+1)}
    queue = [start]
    visited[start] = True

    while len(queue) > 0:
        current = queue.pop(0)
        for nxt in graph[current]:
            if not visited[nxt]:
                queue.append(nxt)
                visited[nxt] = True
                stack += 1
    return stack

print(bfs(graph))