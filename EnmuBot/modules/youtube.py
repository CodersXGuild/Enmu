import logging
import telegram
from telegram.ext import Updater, CommandHandler
import youtube_dl

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Telegram bot token
TOKEN = "5222559003:AAFURf5sF_rIx-EHeczibLOhTCO9C7kQQnM"

# Create a Telegram bot object
bot = telegram.Bot(token=TOKEN)


def ytdl(update, context):
    """Handler for the /ytdl command"""
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Welcome to the YouTube Downloader function."
                                  "Please send me a YouTube video URL and I'll download the media for you.")


def download_video(url):
    """Download the video from the provided YouTube URL"""
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(id)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_url = info_dict.get("url", None)
        if video_url:
            return video_url


def handle_message(update, context):
    """Handle incoming messages"""
    chat_id = update.effective_chat.id
    message_text = update.message.text

    if message_text.startswith('https://www.youtube.com/') or message_text.startswith('http://www.youtube.com/'):
        video_url = message_text
        download_url = download_video(video_url)

        if download_url:
            context.bot.send_message(chat_id=chat_id, text="Downloading media...")
            context.bot.send_video(chat_id=chat_id, video=download_url)
        else:
            context.bot.send_message(chat_id=chat_id, text="Sorry, I couldn't download the media. Please try again.")
    else:
        context.bot.send_message(chat_id=chat_id, text="Please provide a valid YouTube video URL.")


def main():
    """Main function to start the bot"""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add handlers for commands
    dispatcher.add_handler(CommandHandler("ytdl", ytdl))

    # Add a handler to handle incoming messages
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()
