from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Dictionary to store user progress and wallet
user_data = {}

# Start command
def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    user_data[chat_id] = {'telegram': False, 'twitter_follow': False, 'twitter_retweet': False, 'wallet': None, 'step': 'task'}
    update.message.reply_text(
        "MurG-AI Airdrop Campaign\n\n"
        "Complete the following tasks:\n"
        "1. Join our Telegram Channel: https://t.me/MurGAI_Community\n"
        "2. Follow us on Twitter: https://twitter.com/MurGAI_Official\n"
        "3. Retweet our pinned post: https://x.com/MurGAI_Official/status/1921992357030863241?t=IMSeC_7e0RmZFyaq0hUzTw&s=19"
        "✅ After completing, type: done"
    )

# Handle user responses
def handle_message(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    text = update.message.text.strip().lower()

    # Ensure user started the process
    if chat_id not in user_data:
        update.message.reply_text("Please type /start first to begin the airdrop process.")
        return

    # Handle Task Completion
    if text == 'done' and user_data[chat_id]['step'] == 'task':
        # You can add actual verification here using Twitter/Telegram API if needed
        user_data[chat_id]['step'] = 'wallet'
        update.message.reply_text("✅ Task submission received!\nNow please send your **BEP-20 Wallet Address (BNB Chain)** to get your reward.")
        return

    # Handle Wallet Input
    if user_data[chat_id]['step'] == 'wallet':
        if len(text) == 42 and text.startswith('0x'):
            user_data[chat_id]['wallet'] = text
            user_data[chat_id]['step'] = 'done'
            update.message.reply_text("✅ Wallet received successfully!\nYou'll get your reward after verification and distribution.")
            print(f"User {chat_id} | Wallet: {text}")
        else:
            update.message.reply_text("❌ Invalid wallet address.\nPlease send a valid BEP-20 address starting with 0x...")
        return

    # Final message
    if user_data[chat_id]['step'] == 'done':
        update.message.reply_text("✅ You've already completed all steps. Please wait for the airdrop distribution.")
    else:
        update.message.reply_text("Type 'done' after finishing all the tasks.")

# Main Function
def main():
    updater = Updater("7238601494:AAGYUYiviwpI5OCbfp8nDnwO_XnXBjCH_f4", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
