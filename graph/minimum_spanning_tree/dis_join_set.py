class DisJoinSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item):
        # we will return the parent of that set
        # if the parent is current element then we will return the current
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])

    def union(self, x_set, y_set):
        # the first thing we nee to find the root of this set
        x_root = self.find(x_set)
        y_root = self.find(y_set)

        # then we need to find the rank of root
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1


vertices = ["A", "B", "C", "D", "E", "F"]


new_disjointset = DisJoinSet(vertices)
new_disjointset.union("A", "B")
new_disjointset.union("A", "C")
print(new_disjointset.find("A"))
