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
        
def main():
    seq = arithmeticSequence(a1=3, d=2, n=6)
    
    print(seq.nth_term())
    print(seq.sum_n_term())


if __name__ == "__main__":
    main()
#####abcduoiuoiuijjj123213oooooooooooo
#123123123123
#123123123123