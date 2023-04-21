import sqlite3 as sql
import PIL as p
import logs 


async def group(chat_id):
    conn = sql.connect('students.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM students_base")
    database = cur.fetchall()
    conn.close()
    flag = 0
    for i in range(411):
        if database[i][0]==chat_id:
            flag = database[i][1]
    
    return flag

async def monday(chat_id):
    st_group = group(chat_id)
    conn = sql.connect(f'rasp/{st_group}.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM monday")
    res = cur.fetchone()
    conn.close()
    s = ''
    j = 0
    for i in ('8:45-10:20', "10:30-12:05", "12:50-14:25", "14:35-16:10", "16:20-17:55"):
        s += f"{i +': ' + res[j]}\n"
        j+=1
    return s

async def tuesday(chat_id):
    st_group = group(chat_id)
    conn = sql.connect(f'rasp/{st_group}.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM tuesday")
    res = cur.fetchone()
    conn.close()
    j = 0
    for i in ('8:45-10:20', "10:30-12:05", "12:50-14:25", "14:35-16:10", "16:20-17:55"):
        s += f"{i +': ' + res[j]}\n"
    return s

async def wednesday(chat_id):
    st_group = group(chat_id)
    conn = sql.connect(f'rasp/{st_group}.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM wednesday")
    res = cur.fetchone()
    conn.close()
    j = 0
    for i in ('8:45-10:20', "10:30-12:05", "12:50-14:25", "14:35-16:10", "16:20-17:55"):
        s += f"{i +': ' + res[j]}\n"
    return s

async def thursday(chat_id):
    st_group = group(chat_id)
    conn = sql.connect(f'rasp/{st_group}.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM thursday")
    res = cur.fetchone()
    conn.close()
    j = 0
    for i in ('8:45-10:20', "10:30-12:05", "12:50-14:25", "14:35-16:10", "16:20-17:55"):
        s += f"{i +': ' + res[j]}\n"
    return s

async def friday(chat_id):
    st_group = group(chat_id)
    conn = sql.connect(f'rasp/{st_group}.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM friday")
    res = cur.fetchone()
    conn.close()
    conn.close()
    j = 0
    for i in ('8:45-10:20', "10:30-12:05", "12:50-14:25", "14:35-16:10", "16:20-17:55"):
        s += f"{i +': ' + res[j]}\n"
    return s

async def saturday(chat_id):
    st_group = group(chat_id)
    conn = sql.connect(f'rasp/{st_group}.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM saturday")
    res = cur.fetchone()
    conn.close()
    conn.close()
    j = 0
    for i in ('8:45-10:20', "10:30-12:05", "12:50-14:25", "14:35-16:10", "16:20-17:55"):
        s += f"{i +': ' + res[j]}\n"
    return s

async def marks(chat_id):
    conn = sql.connect('students.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM students_marks")
    database = cur.fetchall()
    conn.close()
    for i in range(411):
        if database[i][0]==chat_id:
            res = database[i]
    s = ''
    middle_with = 0
    middle_without = 0
    count_with = 0

    #Матан

    math11 = [int(x) for x in res[1].split()]
    math12 = [int(x) for x in res[2].split()]
    s += f"Оценка за курс 'Мат.анализ 1': \n\nЗачёт: {(math11[len(math11)-1]!='3')*'не' + 'зачёт'};\nПопыток использовано: {str(len(math11))}\nЭкзамен: {str(math12[len(math12)-1])}; попыток использовано: {str(len(math12))}\n\n"
    middle_with += sum(math12)
    middle_without += math12[len(math12)-1]

    #Линал

    lin11 = [int(x) for x in res[3].split()]
    lin12 = [int(x) for x in res[4].split()]
    s += f"Оценка за курс 'Алгебра и геометрия': \n\nЗачёт: {(lin11[len(lin11)-1]!='3')*'не' + 'зачёт'};\nПопыток использовано: {str(len(lin11))}\nЭкзамен: {str(lin12[len(lin12)-1])}; попыток использовано: {str(len(lin12))}\n\n"
    middle_with += sum(lin12)
    middle_without += lin12[len(lin12)-1]

    #Прак

    prak = [int(x) for x in res[5].split()]
    s += f"Оценка за курс 'Практикум на ЭВМ': {prak[len(prak)-1]};\nПопыток использовано: {str(len(prak))}\n\n"    
    middle_with += sum(prak)
    middle_without += prak[len(math12)-1]

    #Алгоритмы

    algo = [int(x) for x in res[6].split()]
    s+= f"Оценка за курс 'Алгоритмы и алгоритмические языки': {algo[len(algo)-1]};\nПопыток использовано: {str(len(algo))}\n\n"
    middle_with += sum(algo)
    middle_without += algo[len(algo)-1]

    #История

    hist = [int(x) for x in res[7].split()]
    s += f"Оценка за курс 'История': {hist[len(hist)-1]};\nПопыток использовано: {str(len(hist))}\n\n"    
    middle_with += sum(hist)
    middle_without += hist[len(hist)-1]

    #БЖД

    bzhd = [str(x) for x in res[8].split()]
    s += f"Оценка за курс 'Безопасность жизнедеятельности': {(bzhd[len(bzhd)-1]=='2')*'не' + 'зачёт'};\nПопыток использовано: {str(len(bzhd))}\n\n"    

    #Англ

    eng = [str(x) for x in res[9].split()]
    s += f"Оценка за курс 'Английский язык': {(eng[len(eng)-1]=='2')*'не' + 'зачёт'};\nПопыток использовано: {str(len(eng))}\n\n"    

    #Дискра

    dm = []
    if group(chat_id)=='141':
        dm = [int(x) for x in res[10].split()]
        s += f"Оценка за курс 'Дискретная математика 1': {dm[len(dm)-1]};\nПопыток использовано: {str(len(dm))}\n\n"    
        middle_with += sum(dm)
        middle_without += dm[len(dm)-1]
    #Физра

    pe = [int(x) for x in res[11].split()]
    s += f"Оценка за курс 'Физическая культура': {(pe[len(pe)-1]==2)*'не'*'зачёт'};\nПопыток использовано: {str(len(pe))}\n\n"    

    #Средний балл

    middle_with /= (len(lin12) + len(math12) + len(prak)+len(algo)+len(hist)+len(dm))
    middle_without /= (5+(len(dm)!=0))
    
    s += f"Ваш средний балл с учетом пересдач: {str(middle_with)}\n"
    s += f"Ваш средний балл без учета пересдач: {str(middle_without)}\n"

    return s

async def registered(chat_id):
    conn = sql.connect('registered.db')
    cur = conn.cursor()
    database = cur.fetchall()
    if database.count(chat_id)==0:
        cur.execute("INSERT INTO regs VALUES(?);", chat_id)
        conn.commit()
    conn.close()

async def admin(chat_id):
    conn = sql.connect('admins.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM admins")

    admins = cur.fetchall()
    conn.close()
    return (admins.count(chat_id)>0)

async def all_registered():
    conn = sql.connect('registered.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regs")
    admins = cur.fetchall()
    conn.close()
    return admins

async def homeworks_view(chat_id,mess):
    check = logs.check(chat_id)
    gr = group(chat_id)
    if check=='change':
        logs.write(chat_id,mess)
        return 0
    conn = sql.connect(f'{mess}.db')
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {str(group(chat_id))}")
    f = str(cur.fetchall())
    l = f[len(f)-1]
    conn.close()
    return l

async def homeworks_write(chat_id, mess_id):
    ch = logs.check(chat_id)
    conn = sql.connect(f'{ch}.db')
    cur = conn.cursor()
    l = mess_id,chat_id
    cur.execute(f"INSERT INTO {group(chat_id)} VALUES(?,?);", l)
    conn.commit()
    conn.close()

