import re
from feed import *

filename = "main.txt"

FILE = open(filename, "r")
content = FILE.read()
FILE.close()

f = Feed(content)
#print f.version, f.title, f.logo, f.background, len(f.items)
for item in f.items:
  print item.URL
# attempt to find feed item chunks using reg ex..
reg = "^type="

matches = re.finditer(reg, content, re.M)
if matches == None:
  print "none found"
else:
  lastpos = 0
  for match in matches:
    if lastpos > 0:
      # collect feed item
      #print "last post = " + str(lastpos) + " to " + str(match.start())
      newlen = match.start() - lastpos
      #print content[lastpos:match.start()]
      item = FeedItem(content[lastpos:match.start()])
      #print item.name
    lastpos = match.start()

  # try to get the last chunk...
  #item = FeedItem(content[lastpos:len(content)])
  #print item.name
