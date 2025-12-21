import arithmeticSequence as arithmetic
import fibonacciSequence as fibonacci

def main():
    seq = arithmetic.arithmeticSequence(a1=3, d=2, n=6)
    
    print(seq.nth_term())

    print(seq.sum_n_term())

    fiboSeq = fibonacci.fibonacciSequence(a0=0, a1=1, n=10)
    print (fiboSeq.nth_term()) 

    print (fiboSeq.sum_n_term()) 

if __name__ == "__main__":
    main()