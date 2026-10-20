from telegram import InlineKeyboardButton, InlineKeyboardMarkup
def formal_source_keyboard():
    keyboard = [
        [InlineKeyboardButton("إظهار المصدر الرسمي", callback_data="formal_source")],
    ]
    return InlineKeyboardMarkup(keyboard)