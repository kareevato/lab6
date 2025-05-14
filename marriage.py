def is_boy(x):
    return x % 2 == 1

def is_girl(x):
    return x % 2 == 0

def dfs(node, adj, visited, component):
    visited[node] = True
    component.append(node)
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor, adj, visited, component)

def main():
    n = int(input("Введіть кількість пар: "))
    edges = []
    nodes = []

    print("Введіть пари по одному рядку:")
    for _ in range(n):
        a, b = map(int, input().split())
        edges.append((a, b))
        if a not in nodes:
            nodes.append(a)
        if b not in nodes:
            nodes.append(b)

    adj = {}
    for node in nodes:
        adj[node] = []

    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    visited = {}
    for node in nodes:
        visited[node] = False

    tribes = []
    for node in nodes:
        if not visited[node]:
            component = []
            dfs(node, adj, visited, component)
            tribes.append(component)

    total_boys = 0
    total_girls = 0
    tribe_counts = []

    for tribe in tribes:
        boys = 0
        girls = 0
        for person in tribe:
            if is_boy(person):
                boys += 1
            else:
                girls += 1
        tribe_counts.append((boys, girls))
        total_boys += boys
        total_girls += girls

    total_pairs = total_boys * total_girls

    internal_pairs = 0
    for boys, girls in tribe_counts:
        internal_pairs += boys * girls

    print("Кількість можливих міжплемінних пар:", total_pairs - internal_pairs)

main()
