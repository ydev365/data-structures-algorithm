#dfs
def dfs(graph,v,visited):
    visited[v]=True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)


graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visited=[False]*9

dfs(graph,1,visited)




#bfs
from collections import deque

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True


graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visited=[False]*9
bfs(graph,1,visited)


#계수정렬
array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count=[0]*(max(array)+1)
for i in range(len(array)):
    count[array[i]]+=1

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')


# 2번째 원소 기준으로 정렬
array=[('바나나',2),('사과',5),('당근',3)]

def setting(data):
    return data[1]

result=sorted(array,key=setting)
print(result)


#정렬 내림차순
a.sort(reverse=True)

# 리스트안에 띄어쓰기 정수로 담을때
a=list(map(int,input().split()))

#이진탐색
def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None

array=[1,3,5,7,9,11,13,15,17,19]
print(binary_search(array,7,0,9)+1)  #인덱스 값에 더하기 1 해주는거 중요





