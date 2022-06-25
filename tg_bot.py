# tg_berkantkzBot_api
#
# telegram bot written in python 
# for publishing post updates
# at t.me/u_berkantkz channel.
#
# work in progress for now.
#

import requests
import os

from yarl import URL

berkantkzBot = os.getenv('berkantkzBot')
url = "https://api.telegram.org/bot" + berkantkzBot + "/sendMessage?chat_id=@u_berkantkz&parse_mode=markdown&text="

#requests.post(url)
