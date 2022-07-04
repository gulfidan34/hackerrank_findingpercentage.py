def percentage(name):

    marks = student_marks[name]
    total_marks = 0
    for mark in marks:
        total_marks += mark

    return format(total_marks/len(marks), '.2f')


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(percentage(query_name))
    
