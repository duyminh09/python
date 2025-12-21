class fibonacciSequence:

    def __init__(self, a0, a1, n):
        self.a0 = a0
        self.a1 = a1
        self.n = n 

    def nth_term(self):
        a, b = self.a0, self.a1
        result = []
        for _ in range(self.n):
            result.append(a)
            a, b = b, a + b
        return result

    def sum_n_term(self):
        return 100

















