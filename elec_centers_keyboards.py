from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_homs_electricity_keyboard():
    
    cleaned_centers = [
        ("مركز المحطة", "center_mahatta"),
        ("مركز الزهراء", "center_zahraa"),
        ("مركز الصناعة", "center_sinaha"),
        ("مركز الوعر", "center_waer"),
        ("مركز الشور", "center_shour"),
        ("مركز الريان", "center_rayyan"),
        ("مركز المشاتية", "center_mashatia"),
        ("مركز كرم الزيتون", "center_karam_alzaitoun"),
        ("مركز قطينة", "center_qatina"),
        ("مركز القصير", "center_alqseir"),
        ("مركز جديدة", "center_jadeeda"),
        ("مركز الحواش", "center_alhwash"),
        ("مركز عيون الوادي", "center_ayoun_alwadi"),
        ("مركز القبو", "center_alqabou"),
        ("مركز تل كلخ", "center_tal_kalakh"),
        ("مركز تلبيسة", "center_talbiseh"),
        ("مركز الغنطو", "center_ghanto"),
        ("مركز الرستن", "center_alrastan"),
        ("مركز تلدو", "center_taldu"),
        ("مركز المشرفة", "center_musharifeh"),
        ("مركز المخرم", "center_makhram"),
        ("مركز جب الجراح", "center_jubb_aljarah"),
        ("مركز حسياء", "center_hassia"),
        ("مركز مهين", "center_maheen"),
        ("مركز تدمر", "center_tadmur"),
        ("مركز الفرقلس", "center_alferqlas"),
        ("مركز القريتين", "center_alqaryatayn"),
        ("مركز صدد", "center_saddad"),
        ("مركز الرقامة", "center_alqama"),
        ("مركز شين", "center_shein"),
        ("مركز الحوز", "center_alhwz")
    ]
    
    # بناء الأزرار (زرين في كل صف)
    keyboard = []
    for i in range(0, len(cleaned_centers), 2):
        row = [
            InlineKeyboardButton(text=cleaned_centers[i][0], callback_data=cleaned_centers[i][1])
        ]
        if i + 1 < len(cleaned_centers):
            row.append(InlineKeyboardButton(text=cleaned_centers[i+1][0], callback_data=cleaned_centers[i+1][1]))
        keyboard.append(row)
        
    return InlineKeyboardMarkup(keyboard)