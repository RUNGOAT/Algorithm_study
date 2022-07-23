students = ['가가가', '나나나', '다다다', '라라라', '마마마', '나나나', '다다다', '다다다',
            '가가가', '다다다', '가가가', '나나나', '다다다', '라라라', '가가가']

students_set = set(students)
student_list = []
student_dict = {}

for student in students_set:
    vote = 0
    for i in range(len(students)):
        if student == students[i]:
            vote += 1            
        student_dict.update({student : vote})

student_sort = {k : v for k, v in sorted(student_dict.items(), key= lambda x : x[1], reverse=True)}
print(student_sort)
