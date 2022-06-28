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

feed = "https://berkantkz.github.io/feed.json"
spotify = "https://open.spotify.com/track/"

berkantkzBot = os.environ('BERKANTKZBOT')

post = requests.get(feed).json()

message = ''

if post[0]['posted'] == True :
    print("posting to telegram")
    message += '\n[' + post[0]['name'] + '](' + post[0]['url'] + ') - '
    message += '__' + post[0]['date'] + '\n__'
    if post[0]['song'] :
        message += "\n[spotify](" + spotify + post[0]['song'] + ")\n"
    message += "\n"
    message += post[0]['content']
    print(message)
    url = "https://api.telegram.org/bot" + berkantkzBot + "/sendMessage?chat_id=@u_berkantkz&parse_mode=markdown&text=" + message
    requests.post(url)
else:
    print("nothing to post")
