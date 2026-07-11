class Solution(object):
    def countCompleteComponents(self, n, edges):
        adj={i:[]for i in range(n)}
        res=0
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        vis=[False]*n
        for i in range(n):
            if vis[i]:
                continue
            v,e=self.dfs(i,adj,vis)
            if (v*(v-1))/2==e/2:
                res+=1
        return res
    def dfs(self,i,adj,vis):
        vis[i]=True
        v=1
        e=len(adj[i])
        for el in adj[i]:
            if not vis[el]:
                nv,ne=self.dfs(el,adj,vis)
                v+=nv
                e+=ne
        return v,e

        