import re
from feed import *

filename = "bachl.txt"

FILE = open(filename, "r")
content = FILE.read()
FILE.close()

f = Feed(content)
print "\ncontent: \n"
print f.items[0].type
#print f.version, f.title, f.logo, f.background, len(f.items)
# attempt to find feed item chunks using reg ex..
reg = "^type="

t = "type="
regt = "type=(.+?){1,}"

content2 = f.items[0].content
matches = re.finditer(regt, content2, re.M)
if matches == None:
  print "none found"
else:
  if re.search(regt, content2,re.M)!=None and re.search(regt, content2,re.M).start()>-1:
    print "match result:"
    print re.search(regt, content2,re.M).group(0).replace(t,"")
    print ""
  else:
    print "No Match\n"

  # try to get the last chunk...
  #item = FeedItem(content[lastpos:len(content)])
  #print item.name
