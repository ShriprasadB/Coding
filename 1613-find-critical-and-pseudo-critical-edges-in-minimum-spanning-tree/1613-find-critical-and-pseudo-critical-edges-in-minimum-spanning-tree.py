class DSU:
    def __init__(self,n):
        self.dict1 = list(range(n))

    def find(self, x):
        if x != self.dict1[x]:
            self.dict1[x] = self.find(self.dict1[x])
        return self.dict1[x]

    def union(self, x, y):
        a, b = self.find(x), self.find(y)

        if a == b:
            return False
        else:
            self.dict1[b] = a
            return True
            
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        edges = sorted([(w,u,v,i)for i, (u,v,w) in enumerate(edges)])
        ans1, ans2 = [], []

        for w1,u1,v1,i in edges:
            d1, d2 = DSU(n), DSU(n)
            d1.union(u1,v1)
            t1, t2 = w1, 0
            for w2,u2,v2,j in edges:
                if i == j:
                    continue
                if d1.union(u2,v2): 
                    t1 += w2
                if d2.union(u2,v2):
                    t2 += w2

            if t1 == t2:
                ans1.append(i)
            elif t1 < t2 or d2.union(u1,v1):
                ans2.append(i)

        return [ans2, ans1]





        

        