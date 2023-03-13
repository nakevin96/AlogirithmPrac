def solution(info, edges):
    import sys
    sys.setrecursionlimit(10 ** 6)

    def dfs(node, sheep_count, wolf_count):
        if sheep_count <= wolf_count:
            return 0
        result = sheep_count
        for next_node in node_info[node]:
            is_sheep = True if info[next_node] == 0 else False
            if is_sheep:
                result = max(result, dfs(next_node, sheep_count + 1, wolf_count))
            else:
                result = max(result, dfs(next_node, sheep_count, wolf_count + 1))
        return result

    node_info = [[] for _ in range(len(info))]
    edges.sort(key=lambda x: (x[0], x[1]))
    for source, target in edges:
        node_info[source].append(target)
    return dfs(0, 1, 0)


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
