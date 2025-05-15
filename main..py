from telegram.ext import Updater, CommandHandler

# এখানে আপনার BotFather থেকে নেওয়া টোকেন বসান
TOKEN = 7238601494:AAElbkEz7lEtzYCLubTzphg6DnIGsdQZCWI

def start(update, context):
    update.message.reply_text("স্বাগতম! এটি MurG-AI Giveaway Bot!")

def help_command(update, context):
    update.message.reply_text("Giveaway-তে অংশ নিতে, /join লিখুন!")

def join(update, context):
    user = update.message.from_user
    update.message.reply_text(f"{user.first_name}, আপনি সফলভাবে Giveaway-তে জয়েন করেছেন!")

updater = Updater(TOKEN, use_context=True)

dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help_command))
dp.add_handler(CommandHandler("join", join))

updater.start_polling()
updater.idle()
