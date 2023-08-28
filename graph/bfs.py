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
bfs -> 0 1 2 4 3 5
"""
nodes,edge=map(int, input().split())
# print(type(nodes),edge)
# nodes,edge=input().split(' ')
# nodes,edge=int(nodes),int(edge)

adj_list={}
# print(adj_list)
for _ in range(edge):
    u,v =map(int, input().split())
    tem1,tem2=adj_list.get(u,[]),adj_list.get(v,[])
    tem1.append(v)
    tem2.append(u)
    adj_list[u]=tem1
    adj_list[v]=tem2
    
visited=[0]*nodes

def bfs(src):
    q=[]
    visited[src]=1
    q.append(src)
    while len(q):
        head=q.pop(0)
        print(head, end=' ')
        for adj_node in adj_list[head]:
            if visited[adj_node]==0:
                visited[adj_node]=1
                q.append(adj_node)
    
src=0
bfs(src)
