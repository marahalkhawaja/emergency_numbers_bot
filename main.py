from telegram import  Bot, Update , InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes
from config import BOT_TOKEN
from emergency_data import EMERGENCY_SERVICES
from keyboards import emergency_keyboard
from telegram_api import get_bot

 
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
    # print(f"Received callback query: {query.data} from user: {query.from_user.id}")
    updates_array.append(query.data)
    if(query.data == "electricity_emergency"):
        from elec_centers_keyboards import get_homs_electricity_keyboard
        await query.message.reply_text(
            "اختر مركز الكهرباء الذي ترغب في التواصل معه:",
            reply_markup=get_homs_electricity_keyboard()
        )
        return
    if(query.data == "formal_source"):
        
        prev_query = updates_array[-2] if len(updates_array) >= 2 else None
        if prev_query:
            prev_query_formal_source = EMERGENCY_SERVICES.get(prev_query).get("formal_source")
            await query.message.reply_html(
             f"المصدر الرسمي للمعلومات هو:\n\n {prev_query_formal_source}" 
             )
            updates_array.clear()
        
      
    service = EMERGENCY_SERVICES.get(query.data)
    if service:
        await query.message.reply_html(service["message"],reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("إظهار المصدر الرسمي", callback_data="formal_source")]]))
         



def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", handle_start))
    application.add_handler(CallbackQueryHandler(handle_callback_query))
    print("Bot is running...")
    application.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)
    
    import os
    from flask import Flask
    from threading import Thread
    import telebot # Example using pyTelegramBotAPI

    app = Flask('')

    @app.route('/')
    def home():
        return "Bot is alive!"

    def run_server():
        # Render provides the port via environment variables
        port = int(os.environ.get("PORT", 8080))
        app.run(host='0.0.0.0', port=port)

    # Start the web server in a separate thread so it doesn't block the bot
    Thread(target=run_server).start()

    # Initialize and start your Telegram Bot polling or webhooks here
    bot = telebot.TeleBot(os.environ.get("BOT_TOKEN"))
    bot.infinity_polling()

    

if __name__ == "__main__":
    main()

