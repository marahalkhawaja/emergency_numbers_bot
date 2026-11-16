from threading import Thread

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes
from config import API_HOST, API_PORT, BOT_TOKEN
from emergency_data import EMERGENCY_SERVICES
from keyboards import emergency_keyboard
from rest_api import app as rest_api_app

 
updates_array = []
async def handle_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await context.bot.send_message(
        chat_id=chat_id,
        text="أهلاً بك في مساعد الطوارئ لمحافظة حمص.\n\nاختر الخدمة التي تحتاجها:",
        reply_markup=emergency_keyboard(),
        parse_mode=ParseMode.HTML
    )



async def handle_callback_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query is None or query.data is None:
        return

    if context.user_data.get("last_callback_id") == query.id:
        return

    context.user_data["last_callback_id"] = query.id
    await query.answer()
    updates_array.append(query.data)

    if query.data == "electricity_emergency":
        from elec_centers_keyboards import get_homs_electricity_keyboard
        await query.message.reply_text(
            "اختر مركز الكهرباء الذي ترغب في التواصل معه:",
            reply_markup=get_homs_electricity_keyboard(),
        )
        return

    if query.data == "formal_source":
        prev_query = updates_array[-2] if len(updates_array) >= 2 else None
        prev_service = EMERGENCY_SERVICES.get(prev_query) if prev_query else None
        if prev_service:
            await query.message.reply_html(
                f"المصدر الرسمي للمعلومات هو:\n\n{prev_service.get('formal_source', 'لا توجد معلومات رسمية.') }"
            )
        updates_array.clear()
        return

    service = EMERGENCY_SERVICES.get(query.data)
    if service:
        await query.message.reply_html(
            service["message"],
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("إظهار المصدر الرسمي", callback_data="formal_source")]
            ]),
        )



def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", handle_start))
    application.add_handler(CallbackQueryHandler(handle_callback_query))

    api_thread = Thread(
        target=lambda: rest_api_app.run(
            host=API_HOST,
            port=API_PORT,
            debug=False,
            use_reloader=False,
        ),
        daemon=True,
    )
    api_thread.start()

    print(f"REST API is listening on {API_HOST}:{API_PORT}")
    print("Bot is running...")
    application.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)
    
   
if __name__ == "__main__":
    main()
