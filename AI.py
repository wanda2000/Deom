# def bfs(g,s):
#     '''BFS算法的运用'''
#     #把第一个遍历的元素分别放入queue和seen（遍历完的节点）列表中
#     queue = []
#     queue.append(s)
#     seen = []
#     seen.append(s)
#
#     #当queue列表中的元素为0时结束循环
#     while len(queue) > 0:
#         #把列表第一个要遍历的元素从queue列表中删除，并返还该对象给vertex
#         vertex = queue.pop(0)
#         #把要删除的元素的相邻的节点在字典中graph中查找并放入变量neighbors
#         neighbors = g[vertex]
#
#         #变量a在列表neighbors遍历
#         for a in neighbors:
#             #如果变量a没在seen列表中把a加入queue和seen列表中
#             if a not in seen:
#                 queue.append(a)
#                 seen.append(a)
#         print(vertex,"->",end='')
# if __name__ == "__main__":
#     graph={
#         "A":["B","C"],
#         "B":["A","C","D"],
#         "C":["A","B","D","E"],
#         "D":["B","C","E","F"],
#         "E":["C","D"],
#         "F":["D"]
#     }
# bfs(graph,"A")

def DFS(g,s):
    queue=[]
    queue.append(s)
    seen=[]
    seen.append(s)

    while len(queue) > 0:
        v = queue.pop(-1)
        negihbors = g[v]

        for i in negihbors:
            if i not in seen:
                queue.append(i)
                seen.append(i)
        print(v)
if __name__ == "__main__":
    graph = {
        "A":["B","C"],
        "B":["A","C","D"],
        "C":["A","B","D","E"],
        "D":["B","C","E","F"],
        "E":["C","D"],
        "F":["D"]
    }

DFS(graph,"A")
