from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# === Replace these with your project details ===
BOT_TOKEN = "7238601494:AAElbkEz7lEtzYCLubTzphg6DnIGsdQZCWI"
TELEGRAM_CHANNEL = "https://t.me/MurGAI_Community"
TWITTER_PROFILE = "https://twitter.com/MurGAI_Official"
TWEET_LINK = "https://x.com/MurGAI_Official/status/1921992357030863241?t=CboEs9thhJhVKl7e3NFG4g&s=19"

# === Start Command ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📲 Join Telegram", url=TELEGRAM_CHANNEL)],
        [InlineKeyboardButton("🐦 Follow on Twitter", url=TWITTER_PROFILE)],
        [InlineKeyboardButton("🔁 Retweet This Tweet", url=TWEET_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    message = (
        "🎉 **Welcome to MurG-AI Airdrop Giveaway!** 🎉\n\n"
        "💰 **$5,000 Reward Pool**\n"
        "🥚 **50,000 MurGerAI Tokens**\n\n"
        "✅ Complete the following 3 simple steps:\n"
        "1️⃣ Join our Telegram Community\n"
        "2️⃣ Follow us on Twitter\n"
        "3️⃣ Retweet our Pinned Post\n\n"
        "⚡ Winners will be selected randomly after campaign ends.\n"
        "📌 Stay active to increase your chances!"
    )

    await update.message.reply_text(
        message,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# === Main App ===
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()
