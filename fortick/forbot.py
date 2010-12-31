import urllib
import json
import mwclient
import time

# fetch link
fetch_discussions = 'http://poker.bitcoinvegas.com/discussions.json'
# how many posts to show on the front page
num_posts_show = 5
# how often to re-update the page
update_speed = 10
bot_login = 'XXXX'
bot_padd = 'XXXX'

while True:
    discuss = urllib.urlopen(fetch_discussions)
    discuss = json.loads(discuss.read())['Discussions']

    text = u''
    for d in discuss[:num_posts_show]:
        poster = d['LastName']
        if poster is None:
            poster = d['FirstName']
        text += u"<span class=\"plainlinks\">[http://poker.bitcoinvegas.com/discussion/%s %s]</span> by '''%s''' &ndash; %s comments\n\n"%(d['DiscussionID'], d['Name'], poster, d['CountComments'])

    site = mwclient.Site('poker.bitcoinvegas.com', path='/wiki/')
    site.login(bot_login, bot_pass)
    page = site.Pages['Template:MainPage_LatestPosts']
    #page = site.Pages['Sandbox']
    #text = page.edit()
    page.save(text)

    time.sleep(update_speed)

