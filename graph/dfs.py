nodes,edges=map(int,input().split())
adj_list={}
for _ in range(edges):
    u,v=map(int, input().split())
    a,b=adj_list.get(u,[]),adj_list.get(v,[])
    a.append(v)
    b.append(u)
    adj_list[u]=a
    adj_list[v]=b

"""
0 ---- 1 ----- 2 ----- 3
       |       |
       |       |
       4 ----- 5

6 6

0 1
1 2
1 4
2 3
2 5
4 5

ROOT: 0
dfs -> 0 1 2 3 5 4
"""

visited=[0]*nodes

def dfs(node):
    print(node, end=' ')
    visited[node]=1
    
    for adj_node in adj_list[node]:
        if visited[adj_node]==0:
            dfs(adj_node)
            
node=0
dfs(node)