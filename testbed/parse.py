import re
from feed import *

filename = "bachl.txt"

FILE = open(filename, "r")
content = FILE.read()
FILE.close()

f = Feed(content)
#print f.version, f.title, f.logo, f.background, len(f.items)
for item in f.items:
  print item.URL
# attempt to find feed item chunks using reg ex..
reg = "^type="

t = "type="
regt = "type=(.+?){1,}"

matches = re.finditer(regt, content, re.M)
if matches == None:
  print "none found"
else:
  if re.search(regt, content,re.M)!=None and re.search(regt, content,re.M).start()>0:
    print re.search(regt, content,re.M).group(0).replace(t,"")

  # try to get the last chunk...
  #item = FeedItem(content[lastpos:len(content)])
  #print item.name
