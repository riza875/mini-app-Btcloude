import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ══════════════════════════════════════════════
#  KONFIGURASI — ganti TOKEN dengan token baru
# ══════════════════════════════════════════════
BOT_TOKEN = "GANTI_DENGAN_TOKEN_BOT_KAMU"
MINI_APP_URL = "https://mini-app-btcloude.vercel.app"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.first_name or "Miner"

    keyboard = [[
        InlineKeyboardButton(
            text="⛏️ Buka BTcloude Mining",
            web_app=WebAppInfo(url=MINI_APP_URL)
        )
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"🪙 Halo *{name}*\\!\n\n"
        f"Selamat datang di *BTcloude Mining*\\!\n"
        f"Klik tombol di bawah untuk mulai menambang BTC\\.",
        parse_mode="MarkdownV2",
        reply_markup=reply_markup
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⛏️ *BTcloude Mining Bot*\n\n"
        "/start — Buka aplikasi mining\n"
        "/help — Bantuan",
        parse_mode="Markdown"
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    print("✅ BTcloude Bot berjalan...")
    app.run_polling()
