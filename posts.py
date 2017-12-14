import pandas as pd
import requests
import datetime
from bs4 import BeautifulSoup

def getSoupObj(url):
    result = requests.get(url)
    c = result.content
    soup = BeautifulSoup(c)
    return soup
    



thread_url = "http://www.eap-forums.gr/modules.php?name=Forums&file=viewtopic&t=35188"#http://www.eap-forums.gr/" + topic_links[23].attrs['href']

thread_soup = getSoupObj(thread_url)


usernames = thread_soup.findAll("span", { "class" : "name"})
texts = thread_soup.findAll("span", { "class" : "postbody"})
dates = thread_soup.findAll("span", { "class" : "postdetails"})


#print(thread_url)

register_dates = dates[0:len(dates):2]
post_dates = dates[1:len(dates):2]

texts_clean = []
for e in range(len(texts)):
    data = texts[e].get_text().split("_________________")[0]
    if data == '' or data in texts_clean:
        continue
    else:
        texts_clean.append(data)


print
for i in range(len(dates) / 2):
    print("%s\nUsername: %s\nRegistered: %s\nPosts: %s\nComment: %s\nDate: %s\n" % (i+1, usernames[i].get_text(), registration_date(register_dates[i]), posts_count(register_dates[i]), " ".join(texts_clean[i].split()), post_date(post_dates[i])))
