import telebot
from telebot import types
bot = telebot.TeleBot('829302822:AAGd6jnAj8LV-FKt-Cw8Dv27Xk4RmgRlBuE')

#Кнопки для выбора города
cityKeys = types.InlineKeyboardMarkup()
callback_button = types.InlineKeyboardButton(text="Москва", callback_data="msk")
callback_button2 = types.InlineKeyboardButton(text="Санкт-Петербург", callback_data="spb")
cityKeys.add(callback_button)
cityKeys.add(callback_button2)

#Кнопки для выбора объекта в МСК
artKeysMsk = types.InlineKeyboardMarkup()
artButtonMsk1 = types.InlineKeyboardButton(text='Объект 1 (м.Лубянка)', callback_data='artobjectMsk1')
artButtonMsk2 = types.InlineKeyboardButton(text='Объект 2 (м.Арбатская)', callback_data='artobjectMsk2')
artButtonMsk3 = types.InlineKeyboardButton(text='Объект 3 (м.Пушкинская)', callback_data='artobjectMsk3')
artButtonMsk4 = types.InlineKeyboardButton(text='Объект 4 (м.Чистые пруды)', callback_data='artobjectMsk4')
artButtonMsk5 = types.InlineKeyboardButton(text='Объект 5 (м.Полянка)', callback_data='artobjectMsk5')
artKeysMsk.add(artButtonMsk1)
artKeysMsk.add(artButtonMsk2)
artKeysMsk.add(artButtonMsk3)
artKeysMsk.add(artButtonMsk4)
artKeysMsk.add(artButtonMsk5)

#Кнопки для выбора объекта в СПб
artKeysSpb = types.InlineKeyboardMarkup()
artButtonSpb1 = types.InlineKeyboardButton(text='limbo* - Система ГиП (м.Спасская)', callback_data='artobjectSpb1')
artButtonSpb2 = types.InlineKeyboardButton(text='limbo* - Не спи. Досыпай. (м.Спасская)', callback_data='artobjectSpb2')
artButtonSpb3 = types.InlineKeyboardButton(text='limbo* - Голой статистикой сложно манипулировать (м.Васелиостровская)', callback_data='artobjectSpb3')
artButtonSpb4 = types.InlineKeyboardButton(text='limbo* - Красивая картина раскрываемости (м.Приморская)', callback_data='artobjectSpb4')
#artButtonSpb5 = types.InlineKeyboardButton(text='Объект 5 (м.Спортивная)', callback_data='artobjectSpb5')
artKeysSpb.add(artButtonSpb1)
artKeysSpb.add(artButtonSpb2)
artKeysSpb.add(artButtonSpb3)
artKeysSpb.add(artButtonSpb4)
#artKeysSpb.add(artButtonSpb5)

@bot.message_handler(commands=['start'])
def start_message(message):
    '''Стартовое сообщение с выбором города'''
    bot.send_message(message.chat.id, 'Здравствуйте, уважаемый '
                                      'ART-потребитель. Это бот Лето228. '
                                      'И этот бот поможет вам найти в вашем городе '
                                      'наши закладки с актуальным искусством.'
                                      '...')
    bot.send_message(message.chat.id, 'Выберите город:', reply_markup=cityKeys)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    '''Обработка нажатий на кнопки'''
    if call.message:
        #кнопки городов
        if call.data == "msk":
            bot.send_message(chat_id=call.message.chat.id, text='Вы выбрали город: Москва')
            #bot.send_message(chat_id=call.message.chat.id, text='Выберете предмет искусства: ', reply_markup=artKeysMsk)
            bot.send_message(chat_id=call.message.chat.id, text='В данный момент в Москве ничего нет. Попробуйте позже')
        elif call.data == "spb":
            bot.send_message(chat_id=call.message.chat.id, text='Вы выбрали город: Санкт-Петербург')
            bot.send_message(chat_id=call.message.chat.id, text='Выберете предмет искусства: ', reply_markup=artKeysSpb)

        #Обработка кнопок артобъектов в спб
        elif call.data == "artobjectSpb1":
            bot.send_message(chat_id=call.message.chat.id, text='Вы выбрали: limbo* - Система ГиП')
            bot.send_message(chat_id=call.message.chat.id, text='%адрес')
            ph = open('artobjectSpb1_klad.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=ph)
            bot.send_message(chat_id=call.message.chat.id, text='Рядом с работой вы найдёте команду для бота. Введите её '
                             ', чтобы получить аудиофайл с комментарием от автора и приглашение на нашу закрытую выставку')
            ph.close()
        elif call.data == "artobjectSpb2":
            bot.send_message(chat_id=call.message.chat.id, text='Вы выбрали: limbo* - Не спи. Досыпай.')
            bot.send_message(chat_id=call.message.chat.id, text='%адрес')
            ph = open('artobjectSpb2_klad.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=ph)
            bot.send_message(chat_id=call.message.chat.id, text='Рядом с работой вы найдёте команду для бота. Введите её '
                             ', чтобы получить аудиофайл с комментарием от автора и приглашение на нашу закрытую выставку')
            ph.close()
        elif call.data == "artobjectSpb3":
            bot.send_message(chat_id=call.message.chat.id, text='Вы выбрали: limbo* - Голой статистикой сложно манипулировать')
            bot.send_message(chat_id=call.message.chat.id, text='%адрес')
            ph = open('artobjectSpb3_klad.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=ph)
            bot.send_message(chat_id=call.message.chat.id, text='Рядом с работой вы найдёте команду для бота. Введите её '
                             ', чтобы получить аудиофайл с комментарием от автора')
            ph.close()
        elif call.data == "artobjectSpb4":
            bot.send_message(chat_id=call.message.chat.id,
                             text='Вы выбрали: limbo* - Красивая картина раскрываемости')
            bot.send_message(chat_id=call.message.chat.id, text='%адрес')
            ph = open('artobjectSpb4_klad.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=ph)
            bot.send_message(chat_id=call.message.chat.id,
                             text='Рядом с работой вы найдёте команду для бота. Введите её '
                                  ', чтобы получить аудиофайл с комментарием от автора')
            ph.close()


        else:
            bot.send_message(chat_id=call.message.chat.id, text='Ошибка выбора')


#Команды для находа и ненахода объектов. Копипастой нужно добавить команды для других объектов
#Возможно, лучше поменять описание
@bot.message_handler(commands=['artobjectspb1'])
def artobjectSpb1_nahod(message):
    bot.send_message(message.chat.id, 'Поздравляем! Вы нашли закладку с картиной. '
                                      'Вот что сам автор говорит о своём произведении:')
    au = open('artobjectSpb1_comment.m4a', 'rb')
    bot.send_audio(message.chat.id, audio=au)
    au.close()
@bot.message_handler(commands=['artobjectspb1_nenahod'])
def artobjectSpb1_nenahod(message):
    bot.send_message(message.chat.id, 'К сожалению, у вас ненаход, закладку уже сошкурил кто-то до вас. '
                                      'Для наркопотребителей это не редкое явление. '
                                      'Чтобы вы не расстраивались, мы отправим вам открытку и приглашение на нашу закрытую выставку.')
    au = open('artobjectSpb1_comment.m4a', 'rb')
    ph = open('artobjectSpb1_nenahod.jpg', 'rb')
    bot.send_photo(message.chat.id, photo=ph)
    bot.send_audio(message.chat.id, audio=au)
    au.close()
    ph.close()





bot.polling()