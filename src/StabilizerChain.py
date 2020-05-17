# *-* coding: utf-8 *-*

from utility import *

from Permutation import *
from SchreierTree import *



# Набор данных одного шага алгоритма
class Step:
    
    def __init__(self, stab_point, gen_set, length):
        self.stab_point = stab_point
        self.gen_set = gen_set[::]
        
        if len(gen_set) == 0:
            gen_set.append(Permutation.empty(length))
        
        self.tree = SchreierTree(stab_point, gen_set)



# Цепочка стабилизаторов
class StabilizerChain:
    
    def __init__(self, gen_set):
        if len(gen_set) == 0:
            raise ValueError('Empty set is forbidden')
        
        self.length = max([len(x) for x in gen_set])
        
        # Приводим перестановки к одному размеру
        for x in gen_set:
            x.normalize(self.length)
        
        self.chain = [Step(0, gen_set, self.length)]
        
        for i in range(1, self.length):            
            new_gen_set = self.build_new_gen_set()            
            small_gen_set = list(self.shrink_gen_set(new_gen_set))
            
            self.append(Step(i, small_gen_set, self.length))
            
            if len(small_gen_set) == 0:
                break
        
        self.strong_gen_set = set()
        self.build_strong_gen_set()
    
    
    def __len__(self):
        return len(self.chain)
    
    def __getitem__(self, index):
        return self.chain[index]
    
    def append(self, value):
        self.chain.append(value)
    
    
    # Нахождение образующих Шрайера
    def build_new_gen_set(self):
        new_gen_set = set()
        step = self[-1]
        
        for s in step.gen_set:
            for u in step.tree.orbit:
                h_u = step.tree.conversion[u]
                h_su = step.tree.conversion[s[u]]
                new_gen_set.add(h_su ** (-1) * s * h_u)
        
        return new_gen_set
    
    # Просеивание образующих
    def shrink_gen_set(self, gen_set):
        small_gen_set = set()
        not_stab = [dict() for i in range(self.length)]
        
        for s in gen_set:
            for x in range(self.length):
                if s[x] == x:
                    continue
                
                if s[x] in not_stab[x]:
                    s = s ** (-1) * not_stab[x][s[x]]
                else:
                    not_stab[x][s[x]] = s
                    small_gen_set.add(s)
                    break
        
        return small_gen_set
    
    # Построение сильного порождающего множества
    def build_strong_gen_set(self):
        for step in self.chain:
            for edge in step.tree.data:
                if edge[1] == None:
                    continue
                sigma = step.gen_set[edge[1]] ** -1
                self.strong_gen_set.add(sigma)
    
    
    # Порядок построенной группы
    def ord(self):
        order = 1
        for step in self.chain:
            order *= len(step.tree)
        return order
    
    
    # Орбита элемента x в построенной группе
    def get_orbit(self, x):
        x -= 1
        for step in self.chain:
            if x in step.tree.orbit:
                return plus(step.tree.orbit)
        return set([x + 1])
    
    
    # Порождающие Stab_{1, ..., index}
    def get_gen_set(self, index):
        return self[index].gen_set
    
    
    # Сильное порождающее множество
    def get_strong_gen_set(self):
        return self.strong_gen_set
    
    
    # Содержится ли sigma в построенной группе
    # Разложение через элементы сильного порождающего множества, если need_decomp = True
    def contains(self, sigma, need_decomp = False):
        sigma.normalize(self.length)
        
        s = sigma
        decomp = []
        
        for step in self.chain:
            u = s[step.stab_point]
            if u not in step.tree.orbit:
                return False
            
            h_u = step.tree.get_conversion(u)
            s = h_u * s
            
            if h_u != Permutation.empty(self.length):
                decomp.append(h_u ** (-1))
        
        if need_decomp:
            return decomp
        
        return True