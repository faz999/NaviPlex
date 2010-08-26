import urllib

main = "http://www.navi-x.org/playlists/med_port.plx"
networks = "http://www.box.net/rssdownload/438209877/index.plx"
shows = "http://website.navi-x.org/-networks/TV_Shows/index.plx"
cbs = "http://navix.turner3d.net/scrape/cbs/"

print urllib.urlopen(cbs).read()
