# *-* coding: utf-8 *-*

from utility import *



# Цикл
class Cycle:
    
    @staticmethod
    def empty():
        return Cycle([])
    
    def __init__(self, data):
        self.data = data[::]
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __setitem__(self, index, value):
        self.data[index] = value
        return self.data[index]
    
    def append(self, value):
        self.data.append(value)
    
    # Вывод на экран
    def __str__(self):
        return '(' + ' '.join(map(str, self.data)) + ')'
    
    def __repr__(self):
        return str(self) 
    
    # Приведение к виду перестановки
    def to_permutation(self, length = 0):
        if len(self.data) == 0:
            raise ValueError('Empty cycles are forbidden')
        
        length = max(length, max(self.data) + 1)
        
        res = Permutation.empty(length)
        for i in range(len(self)):
            res[self[i]] = self[(i + 1) % len(self)]
        
        return res
    
    # Возведение в степень
    def __pow__(self, degree):
        degree %= len(self)
        
        if degree == 0:
            return []
        
        # Возмножно получится несколько циклов
        res = []
        used = [0] * len(self)
        current = Cycle.empty()
        
        for i in range(len(self)):
            if used[i]:
                continue
            
            used[i] = True
            current.append(self[i])
            j = (i + degree) % len(self)
            
            while self[j] != current[0]:
                used[j] = True
                current.append(self[j])
                j = (j + degree) % len(self)
            
            res.append(current)
            current = Cycle.empty()
        
        return res



# Перестановка
class Permutation:
    
    # return id
    @staticmethod
    def empty(length):
        return Permutation([i for i in range(length)])
    
    
    def __init__(self, data):
        # Задать перестановку можно в любой индексации
        data = plus(data, -min(data))
        
        if min(data) != 0 or max(data) != len(data) - 1:
            raise ValueError('not a permutation')
        
        check = [0] * len(data)
        for i in data:
            check[i] += 1
        if check.count(1) != len(check):
            raise ValueError('not a permutation')
        
        self.data = data[::]
    
    
    def __len__(self):
        return len(self.data)    
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __setitem__(self, index, value):
        self.data[index] = value
        return self.data[index]
    
    def append(self, value):
        self.data.append(value)
    
    # Вывод на экран
    def __str__(self):
        # Как перестановка
        # return str(plus(self.data))
        
        # Как произведение циклов
        res = []
        for c in self.to_cycles():
            if len(c) > 1:
                res.append(str(plus(c)))
                
        if len(res) == 0:
            return 'id'
        return ''.join(res)
    
    def __repr__(self):
        return str(self)
    
    # Для dict()
    def __hash__(self):
        return hash(tuple(self.data))
    
    def __eq__(self, other):
        return self.data == other.data
    
    def copy(self):
        return Permutation(self.data)
    
    # Приведение к нужному размеру
    def normalize(self, length):
        while len(self) < length:
            self.append(len(self))
    
    # Разложение в независимые циклы
    def to_cycles(self):
        res = []
        used = [0] * len(self)
        current = Cycle.empty()
        
        for i in range(len(self)):
            if used[i]:
                continue
            
            used[i] = True
            current.append(i)
            j = self[i]
            
            while j != current[0]:
                used[j] = True
                current.append(j)
                j = self[j]
            
            res.append(current)
            current = Cycle.empty()
        
        return res
    
    # Перемножение
    def __mul__(self, other):
        size = max(len(self), len(other))
        self.normalize(size)
        other.normalize(size)
        
        res = Permutation.empty(len(self))
                
        for i in range(len(self)):
            res[i] = self[other[i]]
        
        return res
    
    # Возведение в степень
    def __pow__(self, degree):
        res = Permutation.empty(len(self))
        
        # Раскладываем на независимые циклы и возводим их в степень
        for x in self.to_cycles():
            # Возможно получилось много циклов из одного
            for cycle in x ** degree:
                for j in range(len(cycle)):
                    res[cycle[j]] = cycle[(j + 1) % len(cycle)]
        
        return res
    
    # Порядок перестановки
    def ord(self):
        mult = 1
        cur_gcd = 0
        
        for cycle in self.to_cycles():
            mult *= len(cycle)
            cur_gcd = gcd(cur_gcd, len(cycle))
        
        return mult // cur_gcd


# Запись вида '(1 2 3)' или [1, 2, 3] интерпретируется как цикл
def to_perm(inp):
    if type(inp) == str:
        inp = list(map(int, inp[1:-1].split()))
        
    return Cycle(plus(inp, -1)).to_permutation()