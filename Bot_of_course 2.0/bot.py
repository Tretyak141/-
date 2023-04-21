import aiogram
from aiogram import types,Bot,Dispatcher,executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,KeyboardButtonPollType
import datetime
import work_with_db_lib as sql
import logs

#Main menu

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

#Data-list menu

menu_student_rasp = [
    ["Понедельник","Вторник","Среда"],
    ["Четверг","Пятница","Суббота"],
    ["Вернуться в главное меню"]
]

#Homeworks menu

menu_student_homeworks = [
    ["АиГ", "Мат.анализ"],
    ["Русский язык", "Дискретная математика"],
    ["Английский язык: начинающие"],
    ["Английский язык: продолжающие"],
    ["Практикум 1"],
    ["Практикум 2"],
    ["Вернуться в главное меню"]
]

#Update menu

menu_student_change = [
    ["Обновить АиГ", "Обновить Мат.анализ"],
    ["Обновить Русский язык", "Обновить Дискретная математика"],
    ["Обновить Английский язык: начинающие"],
    ["Обновить Английский язык: продолжающие"],
    ["Обновить Практикум 1"],
    ["Обновить Практикум 2"],
    ["Вернуться в главное меню"]
]

#Admin menu

menu_admin = [
    ['Расписание'],
    ['Узнать четность недели']
]

#menu of free classes

menu_free1 = [
    ["Пн","Вт","Ср"],
    ["Чт","Пт","Сб"]
]

menu_free2 = [
    ['8:45','10:30'],['12:15','14:35'],['16:20','18:00','19:40']
]

#Keyboards

keyboard_main = types.ReplyKeyboardMarkup(keyboard=menu_student_main)
keyboard_rasp = types.ReplyKeyboardMarkup(keyboard=menu_student_rasp)
keyboard_home = types.ReplyKeyboardMarkup(keyboard=menu_student_homeworks)
keyboard_change = types.ReplyKeyboardMarkup(keyboard=menu_student_change)
keyboard_admin = types.ReplyKeyboardMarkup(keyboard=menu_admin)
keyboard_day = types.ReplyKeyboardMarkup(keyboard=menu_free1)
keyboard_time = types.ReplyKeyboardMarkup(keyboard=menu_free2)

#Start handler

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = str(message.chat.id)
    sql.registered(user_id)
    adm_flag = sql.admin(user_id)
    if adm_flag:
        await message.answer('Выберите то, что вам нужно',reply_markup=keyboard_admin)
    else:
        await message.answer('Привет! Выбери то, что тебе нужно',reply_markup=keyboard_main)


@dp.message_handler(content_types=[
    types.ContentType.PHOTO,
    types.ContentType.TEXT,
    types.ContentType.DOCUMENT
])
async def ans(message: types.Message):
    chat_id = str(message.chat.id)
    adm_flag = sql.admin(chat_id)


    #Admin control
    if adm_flag:
        if message.text=='Расписание':
            await message.answer('Введите номер группы')
        elif message.text=='Узнать четность недели':
            x = datetime.datetime.now()
            l = int(x.strftime("%W"))
            if l%2==1:
                await message.answer('Сейчас четная неделя')
            else:
                await message.answer('Сейчас нечетная неделя')
        elif message.text=='Вернуться в главное меню':
            s = logs.check(chat_id)
            await message.answer('Выберите то, что вам нужно',reply_markup=keyboard_admin)
        else:
            s = logs.check(chat_id)

            if ((int(s)>=101)and(int(s)<=119))or(int(s)==141):
                if message.text=='Понедельник':
                    await message.answer(sql.monday(s),reply_markup=keyboard_admin)
                elif message.text=='Вторник':
                    await message.answer(sql.tuesday(s),reply_markup=keyboard_admin)
                elif message.text=='Среда':
                    await message.answer(sql.wednesday(s),reply_markup=keyboard_admin)
                elif message.text=='Четверг':
                    await message.answer(sql.thursday(s),reply_markup=keyboard_admin)
                elif message.text=='Пятница':
                    await message.answer(sql.friday(s),reply_markup=keyboard_admin)
                elif message.text=='Суббота':
                    await message.answer(sql.saturday(s),reply_markup=keyboard_admin)
                else:
                    await message.answer('Вводите команды корректно')


            elif ((int(message.text)>=101)and(int(message.text)<=119))or(int(message.text)==141):
                logs.write(chat_id,message.text)
                await message.answer('Выберите день недели',reply_markup=keyboard_rasp)
            elif s=='':
                users = sql.all_registered()
                for x in users:
                    bot.forward_message(x,message.chat.id,message.message_id)
            
    #User control

    else:
        days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница","Суббота"]
        subjects = ["АиГ","Мат.анализ","Дискретная математика","Русский язык","Английский язык: начинающие","Английский язык: продолжающие","Практикум 1", "Практикум 2"] 
        txt = message.text
        match txt:
            case 'Расписание':
                await message.answer('Выберите день',reply_markup=keyboard_rasp)
            case 'Понедельник':
                await message.answer(sql.monday,reply_markup=keyboard_main)
            case 'Вторник':
                await message.answer(sql.tuesday,reply_markup=keyboard_main)
            case 'Среда':
                await message.answer(sql.wednesday,reply_markup=keyboard_main)
            case 'Четверг':
                await message.answer(sql.thursday,reply_markup=keyboard_main)
            case 'Пятница':
                await message.answer(sql.friday,reply_markup=keyboard_main)
            case 'Суббота':
                await message.answer(sql.saturday,reply_markup=keyboard_main)
            case subjects.count(txt):
                s = sql.homeworks_view(chat_id,txt)
                if s==0:
                    await message.answer('Введите домашнюю работу')
                else:
                    await bot.forward_message(message.chat.id,s[1],s[0])
            case 'Узнать четность недели':
                x = datetime.datetime.now()
                l = int(x.strftime("%W"))
                if l%2==1:
                    await message.answer('Сейчас четная неделя')
                else:
                    await message.answer('Сейчас нечетная неделя')
            


executor.start_polling(dp)