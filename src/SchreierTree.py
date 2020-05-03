# *-* coding: utf-8 *-*

from utility import *
from Permutation import *



class SchreierTree:
    
    def __init__(self, root, gen_set):
        self.root = root
        self.length = len(gen_set[0])
        self.gen_set = gen_set
        
        self.orbit = set()
        self.data = [[i, None] for i in range(self.length)]
        
        self.build(self.root)
        
        used = [False] * self.length
        # Путь от вершины до корня
        self.conversion = [None] * self.length
        
        for v in self.orbit:
            if not used[v]:
                self.find_conversion(v, used)
    
    
    def __len__(self):
        return len(self.orbit)
    
    
    # Построение дерева
    def build(self, v):
        self.orbit.add(v)
        for i in range(len(self.gen_set)):
            sigma = self.gen_set[i]
            u = sigma[v]
            if u not in self.orbit:
                self.data[u] = [v, i]
                self.build(u)
    
    # Нахождение h_v : h_v(1) = v
    def find_conversion(self, v, used):
        if used[v]:
            return
        
        if v == self.root:
            used[v] = True
            self.conversion[v] = Permutation.empty(self.length)
            return
        
        parent = self.data[v]
        self.find_conversion(parent[0], used)
        
        used[v] = True
        self.conversion[v] = self.gen_set[parent[1]] * self.conversion[parent[0]]
    
    
    # Возвращает h такой, что h(v) = 1
    def get_conversion(self, v):
        return self.conversion[v] ** (-1)
    
    # Элементы, содержащиеся в дереве
    def get_orbit(self):
        return plus(self.orbit)