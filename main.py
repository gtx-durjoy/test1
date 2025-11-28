from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

BOT_TOKEN = "8378713809:AAGvsWfDoQmPqUjBjKopzzyyFA-OvbSYxI4"
def start(update, context):
    update.message.reply_text("🤖 DurjoyTestBot Activated!\nSend me anything & I will repeat.")

def reply(update, context):
    text = update.message.text
    update.message.reply_text(f"Echo: {text}")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
