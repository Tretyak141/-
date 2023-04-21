f = open('students.txt')
m = []
for i in range(411):
    a,b = map(int,f.readline().split())
    m.append(a)
f.close()
for i in range(411):
    l = str(m[i])
    f = open('логи/logs_'+l+'.txt','a')
    f.close()