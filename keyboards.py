
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def emergency_keyboard():
    keyboard = [
        [InlineKeyboardButton("إسعاف مديرية الصحة", callback_data="ambulance")],
        [InlineKeyboardButton("إسعاف الهلال الأحمر", callback_data="red_crescent")],
        [InlineKeyboardButton("الدفاع المدني", callback_data="civil_defense")],
        [InlineKeyboardButton("الطوارئ الأمنية", callback_data="security")],
        [InlineKeyboardButton("الخدمات الفنية", callback_data="technical_services")],
        [InlineKeyboardButton("عمليات فرع المرور (حوادث سير)", callback_data="traffic_accidents")],
        [InlineKeyboardButton("طوارئ الكهرباء", callback_data="electricity_emergency")],
        [InlineKeyboardButton("طوارئ المياه", callback_data="water_emergency")],
        [InlineKeyboardButton("رابط الشكاوي - مديرية الصحة", callback_data="health_complaints")],
        [InlineKeyboardButton("مجلس مدينة حمص", callback_data="city_council")],
    ]
    return InlineKeyboardMarkup(keyboard)
