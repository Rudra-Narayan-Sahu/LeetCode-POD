class Solution(object):
    def remainingMethods(self, n, k, invocations):
        adj=[[] for _ in range(n)]
        #indegree=[0]*n
        suspicious=[False]*n
        for u,v in invocations:
            adj[u].append(v)
        q=deque([k])
        q.append(k)
        suspicious[k]=True
        while q:
            curr=q.popleft()
            for ngbr in adj[curr]:
                if not suspicious[ngbr]:
                    suspicious[ngbr]=True
                    q.append(ngbr)
        res=[]
        cantremove=False
        for u,v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))
        return [i for i in range(n) if not suspicious[i] ]
            
            



        