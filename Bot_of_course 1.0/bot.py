import aiogram
from aiogram import types,Bot,Dispatcher,executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,KeyboardButtonPollType
import datetime


tok = '6105839706:AAGNCmL4kfDXFu4K31Pgg0Ui2qT-KDoxs4s'
bot = Bot(token=tok)
dp = Dispatcher(bot)


menu_student_main = [
    ["Посмотреть расписание"],
    ["Расписание другой группы"],
    ["Узнать четность недели"],
    ["Посмотреть ДЗ",
    "Обновить ДЗ"],
    ["Официально свободные аудитории"],
    ["Мои оценки за сессию"]
]

menu_student_rasp = [
    ["Понедельник","Вторник","Среда"],
    ["Четверг","Пятница","Суббота"],
    ["Вернуться в главное меню"]
]

menu_student_homeworks = [
    ["АиГ", "Мат.анализ"],
    ["Русский язык", "Дискретная математика"],
    ["Английский язык: начинающие"],
    ["Английский язык: продолжающие"],
    ["Практикум 1"],
    ["Практикум 2"],
    ["Вернуться в главное меню"]
]

menu_student_change = [
    ["Обновить АиГ", "Обновить Мат.анализ"],
    ["Обновить Русский язык", "Обновить Дискретная математика"],
    ["Обновить Английский язык: начинающие"],
    ["Обновить Английский язык: продолжающие"],
    ["Обновить Практикум 1"],
    ["Обновить Практикум 2"],
    ["Вернуться в главное меню"]
]

menu_admin = [
    ['Расписание'],
    ['Узнать четность недели']
]

menu_free1 = [
    ["Пн","Вт","Ср"],
    ["Чт","Пт","Сб"]
]

menu_free2 = [
    ['8:45','10:30'],['12:15','14:35'],['16:20','18:00','19:40']
]

keyboard_main = types.ReplyKeyboardMarkup(keyboard=menu_student_main)
keyboard_rasp = types.ReplyKeyboardMarkup(keyboard=menu_student_rasp)
keyboard_home = types.ReplyKeyboardMarkup(keyboard=menu_student_homeworks)
keyboard_change = types.ReplyKeyboardMarkup(keyboard=menu_student_change)
keyboard_admin = types.ReplyKeyboardMarkup(keyboard=menu_admin)
keyboard_day = types.ReplyKeyboardMarkup(keyboard=menu_free1)
keyboard_time = types.ReplyKeyboardMarkup(keyboard=menu_free2)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    a = str(message.chat.id)
    l = open('admins.txt')
    k = [str(x) for x in l.read().split('\n')]
    l.close()
    print(k)
    if not(a in k):
        await message.answer('Привет!',reply_markup=keyboard_main)
        l = open('registered.txt')
        m = [str(x) for x in l.read().split('\n')]
        print(m)
        l.close()
        if not(a in m):
            f = open('registered.txt','a')
            f.write(a+'\n')
            f.close()
        
            f = open(f'student_groups/{str(message.chat.id)}.txt')
            l = f.readline()
            f.close()
            f = open(f'registered_groups/{l}.txt','a')
            f.write(str(message.chat.id)+'\n')
            f.close()
        f = open(f'логи/logs_{message.chat.id}.txt','a')
        f.close()
    else:
        await message.answer('Выберите нужную функцию или отправьте сообщение для рассылки',reply_markup=keyboard_admin)


@dp.message_handler(content_types=[
    types.ContentType.PHOTO,
    types.ContentType.TEXT,
    types.ContentType.DOCUMENT
])
async def ans(message: types.Message):
    a = str(message.from_user.id)
    f = open('admins.txt')
    k = (str(x) for x in f.read().split('\n'))
    f.close()
    if a in k:
        print(message)
        days = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота"]
        days1 = ["Пн","Вт","ср","Чт","Пт","Сб"]
        if message.text=="Расписание":
            await message.answer('Выберите день',reply_markup=keyboard_rasp)
        elif message.text in days:
            await message.answer('Выберите группу')
            f = open(f'logs_adms/{str(message.chat.id)}.txt','a')
            f.write(message.text)
            f.close()
        elif message.text=='Узнать четность недели':
            x = datetime.datetime.now()
            l = int(x.strftime("%W"))
            if l%2==1:
                await message.answer('Сейчас четная неделя')
            else:
                await message.answer('Сейчас нечетная неделя')
        elif message.text=='Вернуться в главное меню':
            await message.answer('Выберите нужную функцию',reply_markup=keyboard_admin)
        else:
            for i in range(101,142):
                if message.text==str(i):
                    f = open(f'logs_adms/{str(message.chat.id)}.txt')
                    l = f.readline()
                    f.close()
                    f = open(f'logs_adms/{str(message.chat.id)}.txt','w+')
                    f.seek(0)
                    f.close()
                    file = open(f'Расписание/{l}{str(i)}.txt')
                    l = file.readline()
                    k = l + '\n'
                    while l!='':
                        l = file.readline()
                        k = k + l + '\n'
                    file.close()
                    await message.answer(k)
                    
            else:
                f = open('registered.txt')
                l = f.readline()
                k = []
                k.append(l)
                while l!='':
                    l = f.readline()
                    l = l.replace('\n','')
                    k.append(l)
                f.close()
                print(k)
                    
                        
    else:
        f = open(f'логи/logs_{str(message.from_user.id)}.txt')
        l = f.readline()
        l = str(l)
        f.close()
        f = open(f'логи/logs_{str(message.from_user.id)}.txt','w+')
        f.seek(0)
        f.close()
        f = open(f'student_groups/{a}.txt')
        a = str(f.readline())
        f.close()
        gr = []
        for i in range(101,120):
            gr.append(str(i))
        gr.append('141')
        if l!='':
            if l=='Input day':
                f = open(f'логи/logs_{str(message.from_user.id)}.txt','a')
                f.write(f'Input time {message.text}')
                f.close()
                await message.answer('Выберите время',reply_markup=keyboard_time)
            elif message.text=='Вернуться в главное меню':
                f = open(f'логи/logs_{str(message.from_user.id)}.txt','w+')
                f.seek(0)
                f.close()
                await message.answer('Выберите нужную функцию',reply_markup=keyboard_main)
            elif l.count('Input time ')!=0:
                l = l.replace('Input time ','')
                f = open(f'{l}/{message.text}.txt')
                a = f.read()
                f.close()
                await message.answer(a,reply_markup=keyboard_main)
            elif l in gr:
                f = open(f'Расписание/{message.text}{l}.txt')
                k = ''
                m = ['8:45-10:20', "10:30-12:05", "12:50-14:25", "14:35-16:10", "16:20-17:55"]
                for i in range(5):
                    k = k + m[i] + ': ' + f.readline() + '\n'
                f.close()
                await message.answer(k,reply_markup=keyboard_main)
            elif l in ["АиГ","Мат.анализ","Дискретная математика","Русский язык","Английский язык: начинающие","Английский язык: продолжающие","Практикум 1", "Практикум 2"]:
                f = open(f'registered_groups/{a}.txt')
                k = [str(x) for x in f.read().split('\n')]
                print(k)
                print(l,a)
                f = open(f'{l}/{a}.txt','w+')
                f.seek(0)
                f.close()
                f = open(f'{l}/{a}.txt','w+')
                f.seek(0)
                f.close()
                f = open(f'{l}/{a}.txt','a')
                f.write(str(message.message_id)+'\n')
                f.write(str(message.chat.id))
                f.close()
                f = open(f'логи/logs_{str(message.from_user.id)}.txt','w+')
                f.seek(0)
                f.close()
                await message.answer('Обновлено', reply_markup=keyboard_main)
        else:
            f = open(f'student_groups/{message.chat.id}.txt')
            a = str(f.readline())
            f.close()
            days = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота"]
            subjects = ["АиГ","Мат.анализ","Дискретная математика","Русский язык","Английский язык: начинающие","Английский язык: продолжающие", "Практикум 1", "Практикум 2"]
            if message.text in days:
                file = open(f'Расписание/{message.text}{a}.txt')
                k = ''
                m = ['8:45-10:20', "10:30-12:05", "12:50-14:25", "14:35-16:10", "16:20-17:55"]
                for i in range(5):
                    k = k + m[i] + ': ' + file.readline() + '\n'
                file.close()
                await message.answer(k)
            elif message.text in subjects:
                file = open(f'{message.text}/{a}.txt')
                l = file.readline()
                k = file.readline()
                file.close()
                await bot.forward_message(message.chat.id,from_chat_id=k,message_id=l)
            elif message.text=="Посмотреть расписание":
                await message.answer('Выберите день недели',reply_markup=keyboard_rasp)
            elif message.text=='Расписание другой группы':
                await message.answer('Введите номер группы группы')
            elif message.text in gr:
                await message.answer('Выберите день',reply_markup=keyboard_rasp)
                f = open(f'логи/logs_{str(message.chat.id)}.txt','a')
                f.write(message.text)
                f.close()
            elif message.text=="Официально свободные аудитории":
                await message.answer('Выберите день',reply_markup=keyboard_day)
                f = open(f'логи/logs_{message.chat.id}.txt','a')
                f.write('Input day')
                f.close()
            elif message.text=='Мои оценки за сессию':
                f = open(f'marks/{str(message.chat.id)}.txt')
                a = f.read()
                f.close()
                await message.answer(a)
            elif message.text=="Посмотреть ДЗ":
                await message.answer('Выберите предмет',reply_markup=keyboard_home)
            elif message.text=="Обновить ДЗ":
                await message.answer('Выберите предмет',reply_markup=keyboard_change)
            elif message.text=='Вернуться в главное меню':
                await message.answer('Выберите нужную функцию',reply_markup=keyboard_main)
                f = open(f'логи/logs_{str(message.from_user.id)}.txt','w+')
                f.seek(0)
                f.close()
            elif message.text=='Узнать четность недели':
                x = datetime.datetime.now()
                l = int(x.strftime("%W"))
                if l%2==1:
                    await message.answer('Сейчас четная неделя')
                else:
                    await message.answer('Сейчас нечетная неделя')
            elif message.text.count('Обновить ')!=0:
                a = open(f'логи/logs_{str(message.from_user.id)}.txt','a')
                l = message.text
                l = l.replace('Обновить ','')
                a.write(l)
                a.close()
                await message.answer('Введите ДЗ')
            else:
                await message.answer('Вводите команды корректно',reply_markup=keyboard_main)
executor.start_polling(dp)
