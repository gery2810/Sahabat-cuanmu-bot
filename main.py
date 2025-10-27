import os
from fastapi import FastAPI, Request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from telegram.constants import ParseMode

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8233135065:AAGGTHfUNJBYVAO4s2uxaDIiThb7V4_xGi0")
app = FastAPI()
application = Application.builder().token(BOT_TOKEN).build()

async def start(update: Update, _):
    kb = [
        [InlineKeyboardButton("💬 Basic 1 Jam – Rp5.000", callback_data="buy:basic")],
        [InlineKeyboardButton("📊 Daily Pass – Rp10.000", callback_data="buy:daily")],
        [InlineKeyboardButton("ℹ️ Cek Status", callback_data="status")]
    ]
    await update.message.reply_text(
        "Hai! Selamat datang di *Sahabat Cuanmu* 👋\nPilih paket di bawah untuk mulai konsultasi.",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup(kb)
    )

application.add_handler(CommandHandler("start", start))

@app.post("/telegram/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    await application.update_queue.put(Update.de_json(data, application.bot))
    return {"ok": True}

@app.on_event("startup")
async def startup_event():
    print("Bot started. Set your webhook on Telegram API manually.")
