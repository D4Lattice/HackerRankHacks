#given 2 triplets, compare the scores pair-wise and return the winner on comparison
import os

def compareTriplets(a, b):
    zipped = zip(a,b)
    alice = 0
    bob = 0
    
    for x in zipped:
        if x[0] > x[1]:
            alice += 1
        elif x[0] < x[1]:
            bob += 1 
    return(alice,bob)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
