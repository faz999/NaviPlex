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
    if re.search(self.regv, content,re.M)!=None and re.search(self.regv, content,re.M).start()>0:
      self.version = re.search(self.regv, content,re.M).group(0).replace(self.v,"")
    if re.search(self.regt, content,re.M)!=None and re.search(self.regt, content,re.M).start()>0:
      self.title = re.search(self.regt, content,re.M).group(0).replace(self.t,"")
    if re.search(self.regl, content,re.M)!=None and re.search(self.regl, content,re.M).start()>0:
      self.logo = re.search(self.regl, content,re.M).group(0).replace(self.l,"")
    if re.search(self.regb, content,re.M)!=None and re.search(self.regb, content,re.M).start()>0:
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
  regt = "[^#]type=(.+?){1,}"
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

    if re.search(self.regt, content)!=None and re.search(self.regt, content).start()>0:
      self.type = re.search(self.regt, content).group(0).replace(self.t,"")
    if re.search(self.regn, content)!=None and re.search(self.regn, content).start()>0:
      self.name = re.search(self.regn, content).group(0).replace(self.n,"")
    if re.search(self.regu, content)!=None and re.search(self.regu, content).start()>0:
      self.URL = re.search(self.regu, content).group(0).replace(self.u,"")
    if re.search(self.regd, content)!=None and re.search(self.regd, content).start()>0:
      self.description = re.search(self.regd, content).group(0).replace(self.d,"")
    if re.search(self.regi, content)!=None and re.search(self.regi, content).start()>0:
      self.icon = re.search(self.regi, content).group(0).replace(self.i,"")
    if re.search(self.regth, content)!=None and re.search(self.regth, content).start()>0:
      self.thumb = re.search(self.regth, content).group(0).replace(self.th,"")
    if re.search(self.regd, content)!=None and re.search(self.regd, content).start()>0:
      self.date = re.search(self.regd, content).group(0).replace(self.dt,"")


