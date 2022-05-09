#given n students and their exam results, return the average of a students results when given their name as a query to 2 decimal places
#example input
# >3
# >Ami 83 77 70
# >Kenta 66 68 65
# >Rio 94 59 71
# >Ami

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    
    total = 0
    num_of_tests = len(student_marks[query_name])
    
    for val in student_marks[query_name]:
        total += val
    print("{:0.2f}".format(total/num_of_tests))
