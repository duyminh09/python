class arithmeticSequence:
    def __init__(self, a1, n, d):
        self.a1 = a1
        self.n = n
        self.d = d
    
    def nth_term(self):
        return self.a1 + (self.n - 1) * self.d
        
    def sum_n_term(self):
        total = 0
        for i in range(self.n):
            total = total + self.a1 + i * self.d
        return total
        

#####abcduoiuoiuijjj123213oooooooooooo
#123123123123
#123123123123