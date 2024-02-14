

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from server import server
# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(config.DOWNLOAD_LOCATION):
        os.makedirs(config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "X-URL-Uploader",
        bot_token=config.BOT_TOKEN,
        api_id=config.API_ID,
        api_hash=onfig.API_HASH,
        plugins=plugins
    )
    config.AUTH_USERS.add(958850850)
    app.run()
    server()
