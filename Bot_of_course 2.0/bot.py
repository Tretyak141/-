import aiogram
from aiogram import types,Bot,Dispatcher,executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,KeyboardButtonPollType
import datetime
import work_with_db_lib as sql
import logs

#Main menu

tok = '****'
bot = Bot(token=tok)
dp = Dispatcher(bot)

menu_student_main = [
    ["Посмотреть расписание"],
    ["Узнать четность недели"],
    ["Посмотреть ДЗ",
    "Обновить ДЗ"],
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



#Keyboards

keyboard_main = types.ReplyKeyboardMarkup(keyboard=menu_student_main)
keyboard_rasp = types.ReplyKeyboardMarkup(keyboard=menu_student_rasp)
keyboard_home = types.ReplyKeyboardMarkup(keyboard=menu_student_homeworks)
keyboard_change = types.ReplyKeyboardMarkup(keyboard=menu_student_change)

#Start handler

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = str(message.chat.id)
    sql.registered(user_id)
    adm_flag = sql.admin(user_id)
    await message.answer('Привет! Выбери то, что тебе нужно',reply_markup=keyboard_main)


@dp.message_handler(content_types=[
    types.ContentType.PHOTO,
    types.ContentType.TEXT,
    types.ContentType.DOCUMENT
])
async def ans(message: types.Message):
    chat_id = str(message.chat.id)
            
    #User control
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница","Суббота"]
    subjects = ["АиГ","Мат.анализ","Дискретная математика","Русский язык","Английский язык: начинающие","Английский язык: продолжающие","Практикум 1", "Практикум 2"] 
    txt = message.text
    if txt=='Расписание':
        await message.answer('Выберите день',reply_markup=keyboard_rasp)
    elif txt=='Понедельник':
        await message.answer(sql.monday,reply_markup=keyboard_main)
    elif txt=='Вторник':
        await message.answer(sql.tuesday,reply_markup=keyboard_main)
    elif txt=='Среда':
        await message.answer(sql.wednesday,reply_markup=keyboard_main)
    elif txt=='Четверг':
        await message.answer(sql.thursday,reply_markup=keyboard_main)
    elif txt=='Пятница':
        await message.answer(sql.friday,reply_markup=keyboard_main)
    elif txt=='Суббота':
        await message.answer(sql.saturday,reply_markup=keyboard_main)
    elif txt=='Узнать четность недели':
        x = datetime.datetime.now()
        l = int(x.strftime("%W"))
        if l%2==1:
            await message.answer('Сейчас четная неделя')
        else:
            await message.answer('Сейчас нечетная неделя')
    elif txt.count('Обновить'):
        subj = txt.replace('Обновить ','')
        logs.write(chat_id,subj)
        await message.answer('Введите домашнюю работу')
    elif txt=='Посмотреть ДЗ':
        await message.answer('Введите название предмета',reply_markup=keyboard_home)
    elif txt in subjects:
        await bot.forward_message(chat_id,sql.homeworks_view(chat_id,txt)[1],sql.homeworks_view(chat_id,txt)[0])
        await message.answer('ДЗ переслано',reply_markup=keyboard_main)
    elif txt=='Мои оценки за сессию':
        await message.answer(sql.marks(chat_id),reply_markup=keyboard_main)
    else:
        l = logs.check(chat_id)
        if l in subjects:
            sql.homeworks_write(chat_id,message.message_id)
            await message.answer('Запись прошла успешно',reply_markup=keyboard_main)    
executor.start_polling(dp)