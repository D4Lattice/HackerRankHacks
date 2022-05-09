#Given a square matrix, calculate the absolute difference between the sums of its diagonals.
import os

def diagonalDifference(arr):
    length = len(arr)
    countl = 0
    countr = length-1
    totall = 0
    totalr = 0
    
    for x in range(0,length):
        totall += arr[x][countl]
        totalr += arr[x][countr]
        countl += 1
        countr -= 1
    return(abs(totall - totalr))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
