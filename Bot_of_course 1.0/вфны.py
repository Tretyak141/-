a = ["Пн","Вт","Ср","Чт","Пт","Сб"]
b = ['8:45',"10:30","12:15","14:35","16:20","18:00","19:40"]
for i in a:
    for j in b:
        f = open(f'{i}/{j}.txt','a')
        f.write('Будет доступно в течение дня')
        f.close()