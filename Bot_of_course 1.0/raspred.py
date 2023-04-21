a = open('students.txt')

for i in range(411):
    s,g = map(str,a.readline().split())
    f = open(f'student_groups/{s}.txt','a')
    f.write(g)
    f.close()

a.close()