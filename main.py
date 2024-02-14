import telegram
import logging
import pafy

from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

# Define the start command handler
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the video downloader bot!")

# Define the handler for video messages
def video_message_handler(update, context):
    message = update.message
    url = message.text
    video = pafy.new(url)

    # Get the best available video stream
    best = video.getbest()

    # Download the video
    context.bot.send_message(chat_id=message.chat_id, text="Downloading video...")
    best.download(filepath="/tmp")

    # Send the downloaded video to the user
    context.bot.send_video(chat_id=message.chat_id, video=open("/tmp/" + best.filename, "rb"))

def main():
    # Set up the Telegram bot
    bot_token = "5513839264:AAGsLdSpeIMeNmhJusYLZn3BbE2S-PKsXJc"
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    # Add the start command handler
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Add the video message handler
    video_message_handler = MessageHandler(Filters.regex(r'https?://.*'), video_message_handler)
    dispatcher.add_handler(video_message_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()