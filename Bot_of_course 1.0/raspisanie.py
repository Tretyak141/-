for i in range(1,20):
    for j in ("Понедельник","Вторник","Среда","Четверг","Пятница","Суббота"):
        a = open(f'Расписание/{j}{str(i+100)}.txt','w')
        a.write('Актуальное расписание появится здесь 6 февраля. Следите за обновлениями на сайте https://cs.msu.ru/studies/schedule')
        a.close()
for j in ("Понедельник","Вторник","Среда","Четверг","Пятница","Суббота"):
        a = open(f'Расписание/{j}{141}.txt','w')
        a.write('Актуальное расписание появится здесь 6 февраля. Следите за обновлениями на сайте https://cs.msu.ru/studies/schedule')