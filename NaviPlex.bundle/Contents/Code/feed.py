import re

class Feed:
  import re

  v = "version="
  regv = "[^#]version=(.+?){1,}"
  t = "title="
  regt = "[^#]title=(.+?){1,}"
  l = "logo="
  regl = "[^#]logo=(.+?){1,}"
  b = "background="
  regb = "[^#]background=(.+?){1,}"

  version = 0
  logo = None
  background = None
  title = None
  items = None 

  def __init__(self,content):
    self.items = list()
    self.version = 1 # default version number
    lines = content.split('\n')
    if re.search(self.regv, content,re.M)!=None and re.search(self.regv, content,re.M).start()>-1:
      self.version = re.search(self.regv, content,re.M).group(0).replace(self.v,"")
    if re.search(self.regt, content,re.M)!=None and re.search(self.regt, content,re.M).start()>-1:
      self.title = re.search(self.regt, content,re.M).group(0).replace(self.t,"")
    if re.search(self.regl, content,re.M)!=None and re.search(self.regl, content,re.M).start()>-1:
      self.logo = re.search(self.regl, content,re.M).group(0).replace(self.l,"")
    if re.search(self.regb, content,re.M)!=None and re.search(self.regb, content,re.M).start()>-1:
      self.background = re.search(self.regb, content,re.M).group(0).replace(self.b,"")

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
          self.items.append(item)
          #print item.name
        lastpos = match.start()

      # try to get the last chunk...
      item = FeedItem(content[lastpos:len(content)])
      self.items.append(item)

class FeedItem:

  t = "type="
  regt = "type=(.+?){1,}"
  n = "name="
  regn = "[^#]name=(.+?){1,}"
  u = "URL="
  regu = "[^#]URL=(.+?){1,}"
  d = "description="
  regd = "[^#]description=(.+?){1,}"
  i = "icon="
  regi = "[^#]icon=(.+?){1,}"
  th = "thumb="
  regth = "[^#]thumb=(.+?){1,}"
  dt = "date="
  regdt = "[^#]date=(.+?){1,}"

  description = ""
  icon = None
  thumb = None
  name = ""
  URL = ""
  type = None

  def __init__(self,content):
    self.content = content

    if re.search(self.regt, content,re.M)!=None and re.search(self.regt, content,re.M).start()>-1:
      self.type = re.search(self.regt, content,re.M).group(0).replace(self.t,"")
    if re.search(self.regn, content,re.M)!=None and re.search(self.regn, content,re.M).start()>-1:
      self.name = re.search(self.regn, content,re.M).group(0).replace(self.n,"")
    if re.search(self.regu, content,re.M)!=None and re.search(self.regu, content,re.M).start()>-1:
      self.URL = re.search(self.regu, content,re.M).group(0).replace(self.u,"")
    if re.search(self.regd, content,re.M)!=None and re.search(self.regd, content,re.M).start()>-1:
      self.description = re.search(self.regd, content,re.M).group(0).replace(self.d,"")
    if re.search(self.regi, content,re.M)!=None and re.search(self.regi, content,re.M).start()>-1:
      self.icon = re.search(self.regi, content,re.M).group(0).replace(self.i,"")
    if re.search(self.regth, content,re.M)!=None and re.search(self.regth, content,re.M).start()>-1:
      self.thumb = re.search(self.regth, content,re.M).group(0).replace(self.th,"")
    if re.search(self.regd, content,re.M)!=None and re.search(self.regd, content,re.M).start()>-1:
      self.date = re.search(self.regd, content,re.M).group(0).replace(self.dt,"")


