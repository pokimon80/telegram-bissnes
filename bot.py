from telegram.ext import Application, BusinessMessagesDeletedHandler, BusinessMessageEditedHandler
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def on_deleted(update, context):
    ids = update.deleted_business_messages.message_ids
    await context.bot.send_message(
        chat_id=update.deleted_business_messages.chat.id,
        text=f"Удалены сообщения с ID: {ids}"
    )

async def on_edited(update, context):
    new_text = update.edited_business_message.text or "[не текстовое сообщение]"
    await context.bot.send_message(
        chat_id=update.edited_business_message.chat.id,
        text=f"Сообщение было изменено: {new_text}"
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(BusinessMessagesDeletedHandler(on_deleted))
    app.add_handler(BusinessMessageEditedHandler(on_edited))
    app.run_polling()

if __name__ == "__main__":
    main()
