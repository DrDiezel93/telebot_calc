from telebot import TeleBot, types
import logging


TOKEN = '5983502807:AAE7ygaiKzlnyMcZkTuWHMAalS8XhexlUL8'

bot = TeleBot(TOKEN)

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w", format="%(asctime)s %(levelname)s %(message)s", encoding = 'utf-8')

dct = {}


@bot.message_handler(commands=['start', 'help'])
def answer(msg: types.Message):
    dct[msg.from_user.id] = []
    bot.send_message(chat_id=msg.from_user.id, text=f'Добро пожаловать в калькулятор. Введите арифметическую операцию ( + ; - ; * ; / )')


# @bot.message_handler(commands=['log'])
# def answer(msg: types.Message):
#     temp = True
#     tempos = False
#     if temp == div_(msg):
#         bot.send_message(chat_id=msg.from_user.id, text='Деление на ноль')
#     elif tempos == div_(msg):
#         bot.send_message(chat_id=msg.from_user.id, text='Неправильный ввод данных')


@bot.message_handler()
def answer(msg: types.Message):
    text = msg.text
    if text == '+':
        bot.register_next_step_handler(msg, sum_)
        bot.send_message(chat_id=msg.from_user.id, text='Введите слагаемые через пробел ')
        bot.send_message(chat_id=msg.from_user.id, text='Десятичные числа вводятся через (.) точку')
        bot.send_message(chat_id=msg.from_user.id, text='Комплексные числа вводятся в формате: a+bj (без пробелов)')
    elif text == '-':
        bot.register_next_step_handler(msg, sub_)
        bot.send_message(chat_id=msg.from_user.id, text='Введите уменьшаемое и вычитаемое через пробел')
        bot.send_message(chat_id=msg.from_user.id, text='Десятичные числа вводятся через ( . ) точку')
        bot.send_message(chat_id=msg.from_user.id, text='Комплексные числа вводятся в формате: a+bj (без пробелов)')
    elif text == '*':
        bot.register_next_step_handler(msg, mult_)
        bot.send_message(chat_id=msg.from_user.id, text='Введите умножаемое и множитель через пробел')
        bot.send_message(chat_id=msg.from_user.id, text='Десятичные числа вводятся через ( . ) точку')
        bot.send_message(chat_id=msg.from_user.id, text='Комплексные числа вводятся в формате: a+bj (без пробелов)')
    elif text == '/':
        bot.register_next_step_handler(msg, div_)
        bot.send_message(chat_id=msg.from_user.id, text='Введите делимое и делитель через пробел')
        bot.send_message(chat_id=msg.from_user.id, text='Десятичные числа вводятся через ( . ) точку')
        bot.send_message(chat_id=msg.from_user.id, text='Комплексные числа вводятся в формате: a+bj (без пробелов)')
    else:
        bot.send_message(chat_id=msg.from_user.id, text='Вы прислали: ' + msg.text +
                                                        ', а должны были арифметическое действие')


def is_complex(ex):
    flag = True if "j" in ex else False
    if flag:
        return complex(ex)
    return float(ex)


def sum_(msg):
    try:
        a, b = map(is_complex, msg.text.split())
        logging.info(f' Слагаемые {a} и {b}')
        bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {a + b}')
        logging.info(f"Результат сложения: {a + b}")
        bot.send_message(chat_id=msg.from_user.id, text='Введите арифметическую операцию')
    except ValueError:
        logging.error("Неправильный ввод данных",exc_info=True)
        bot.send_message(chat_id=msg.from_user.id, text='Неправильный ввод данных')
        bot.send_message(chat_id=msg.from_user.id, text='Введите арифметическую операцию')


def sub_(msg):
    try:
        a, b = map(is_complex, msg.text.split())
        logging.info(f' Уменьшаемое {a}, вычитаемое {b}')
        bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычитания {a - b}')
        logging.info(f"Результат вычитания: {a - b}")
        bot.send_message(chat_id=msg.from_user.id, text='Введите арифметическую операцию')
    except ValueError:
        logging.error("Неправильный ввод данных",exc_info=True)
        bot.send_message(chat_id=msg.from_user.id, text='Неправильный ввод данных')
        bot.send_message(chat_id=msg.from_user.id, text='Введите арифметическую операцию')


def mult_(msg):
    try:
        a, b = map(is_complex, msg.text.split())
        logging.info(f' Умножаемое: {a}, множитель: {b}')
        bot.send_message(chat_id=msg.from_user.id, text=f'Результат умножения {a * b}')
        logging.info(f"Результат умножения: {a * b}")
        bot.send_message(chat_id=msg.from_user.id, text='Введите арифметическую операцию')
    except ValueError:
        logging.error("Неправильный ввод данных",exc_info=True)
        bot.send_message(chat_id=msg.from_user.id, text='Неправильный ввод данных')
        bot.send_message(chat_id=msg.from_user.id, text='Введите арифметическую операцию')


def div_(msg):
    try:
        a, b = map(is_complex, msg.text.split())
        logging.info(f' Делимиое: {a}, делитель: {b}')
        try:
            bot.send_message(chat_id=msg.from_user.id, text=f'Результат деления {a / b}')
            logging.info(f"Результат деления: {a / b}")
            bot.send_message(chat_id=msg.from_user.id, text='Введите арифметическую операцию')
        except ZeroDivisionError:
            logging.error("Деление на ноль",exc_info=True)
            bot.send_message(chat_id=msg.from_user.id, text='Делить на ноль не рекомендуется')
            bot.send_message(chat_id=msg.from_user.id, text='Введите арифметическую операцию')
    except ValueError:
        logging.error("Неправильный ввод данных",exc_info=True)
        bot.send_message(chat_id=msg.from_user.id, text='Неправильный ввод данных')
        bot.send_message(chat_id=msg.from_user.id, text='Введите арифметическую операцию')


bot.polling()