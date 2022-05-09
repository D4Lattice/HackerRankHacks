#given n competitors and an array A[i] of size n containing each result,
#return the score of the competitor in 2nd place
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    scores_less_max = [y for y in arr if y != max(arr)]
    print(max(scores_less_max))
