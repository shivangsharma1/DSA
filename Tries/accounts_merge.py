from collections import defaultdict


class Unionfind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, n):
        p = self.parent[n]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


class Solution:
    def accountsMerge(self, accounts):
        uf = Unionfind(len(accounts))
        emailtoacc = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailtoacc:
                    uf.union(i, emailtoacc[e])
                else:
                    emailtoacc[e] = i

        emailgroup = defaultdict(list)
        for email, i in emailtoacc.items():
            leader = uf.find(i)
            emailgroup[leader].append(email)

        res = []
        for i, emails in emailgroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailgroup[i]))
        return res


accounts = [
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"],
]
obj = Solution()
obj.accountsMerge(accounts)
