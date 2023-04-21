import aiogram
from aiogram import types,Bot,Dispatcher,executor
import os



tok = '5755748230:AAHHZIt-AM69H3S3nC94v26UpZ0B7ljPlJE'
bot = Bot(token=tok)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(f'Привет, {message.from_user.full_name} \nЧтобы отправить тайное послание своей пассии - напиши "Отправить послание" \nДля проверки своих посланий напиши "Проверить почтовый ящик"')
    a = open('registered_info/registered_usernames.txt')
    flag = True
    k = [x for x in a.readline().split()]
    for l in k:
        if l==message.from_user.username:
            flag=False
            break
    a.close()
    if flag:
        k.append(message.from_user.username)
        print(k)
        a = open('registered_info/registered_usernames.txt','w')
        for x in k:
            a.write(x+'\n')
        a.close()
    a = open('registered_info/registered_ids.txt')
    flag = True
    k = [x for x in a.readline().split()]
    for l in k:
        if l==str(message.from_user.id):
            flag=False
            break
    a.close()
    if flag:
        k.append(message.from_user.id)
        print(k)
        a = open('registered_info/registered_ids.txt','a')
        a.write(str(message.from_user.id) + '\n')
        a.close()
    a = open(f'mailboxes/{message.from_user.username}.txt','a')
    a.close()
@dp.message_handler()
async def ans(message: types.Message):
    if message.text=='Отправить послание':
        await message.reply('Отлично! Введи ее username без @. \nПример: \nВот его/ее username: *сам username*')
    elif message.text.count('Вот его username')!=0:
        a = message.text
        a = a.replace('Вот его username: ','',1)
        file_now = open(f'{message.from_user.username}.txt', 'a')
        file_now.write(a)
        file_now.close()
    elif message.text.count('Вот ее username')!=0:
        a = message.text
        a = a.replace('Вот ее username: ','',1)
        file_now = open(f'sent_now/{message.from_user.username}.txt', 'a')
        file_now.write(a)
        file_now.close()
        k = open('registered_info/registered_usernames.txt')
        l = [x for x in k.readline().split()]
        k.close()
        flag = False
        for x in l:
            if x==a:
                flag=True
                break
        if not(flag):
            await message.reply('К сожалению, он/она не писала мне:( \nНо я все равно отправлю ей твое сообщение: он/она напишет мне и ее будет ждать приятный сюрприз')
        else:
            await message.reply('Отлично. Теперь напиши послание!')
        l = open(f'юзернеймы_приславших/{a}.txt','a')
        l.write(f'{message.from_user.username}'+'\n')
        l.close()
    elif message.text=='Проверить почтовый ящик':
        a = open(f'mailboxes/{message.from_user.username}.txt')
        k = [x for x in a.readline().split()]
        a.close()
        if len(k)==0:
            await message.reply('К сожалению, ваш ящик пуст')
        else:
            for i in k:
                await message.reply(i)
        a = open(f'mailboxes/{message.from_user.username}.txt','a')
        a.seek(0)
        a.close()
    else:
        use_username = open(f'sent_now/{message.from_user.username}.txt')
        idi = use_username.readline()
        use_username.close()
        if idi=='':
            await message.reply('И чего ты требуешь, человек? Я ж машина и ничего не понимаю...')
        else:
            use_username = open(f'sent_now/{message.from_user.username}.txt','w')
            use_username.seek(0)
            use_username.close()
            mailbox = open(f'mailboxes/{idi}.txt','a')
            mailbox.write(message.text + '\n')
            mailbox.close()
            uns = open('registered_info/registered_usernames.txt')
            a = [x for x in uns.readline().split()]
            uns.close()
            ids = open('registered_info/registered_ids.txt')
            b = [x for x in ids.readline().split()]
            ids.close()
            if idi in a:
                m = b[a.index(idi)]
                await bot.send_message(m,'Тебе пришло новое послание')
                a = open(f'юзернеймы_приславших/{message.from_user.username}.txt')
                k = [x for x in a.readline().split()]
                a.close()
                if idi in k:
                    await message.reply('Поздравляю: у вас взаимная симпатия! Сейчас же уведомлю твою пассию об этом!')
                    await bot.send_message(m,'Похоже, у вас взаимная симпатия с @{message.from_user.username}. Вот его послание: \n{message.text} \n\nСейчас же в личку!')

            await message.reply('Послание отправлено!')                
executor.start_polling(dp)
