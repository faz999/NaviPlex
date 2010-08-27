import urllib
from feed import * 

main = "http://www.navi-x.org/playlists/med_port.plx"
networks = "http://www.box.net/rssdownload/438209877/index.plx"
shows = "http://website.navi-x.org/-networks/TV_Shows/index.plx"
cbs = "http://navix.turner3d.net/scrape/cbs/"

content = urllib.urlopen(networks).read()

feed = Feed(content)
print len(feed.items)
for item in feed.items:
  print item.type, item.name, item.thumb, item.icon, item.URL
  print ""
