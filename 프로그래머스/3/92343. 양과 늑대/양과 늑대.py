def solution(info, edges):
    visited = [False] * len(info)
    visited[0] = True
    global answer
    answer = 0
    
    def dfs(sheep, wolf):
        global answer
        if sheep > wolf:
            answer = max(answer, sheep)
        else:
            return
    
        for edge in edges:
            parent, child = edge
            if visited[parent] and not visited[child]:
                visited[child] = True
                if info[child] == 0:
                    dfs(sheep + 1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[child] = False
        
    dfs(1, 0)
    
    return answer
        