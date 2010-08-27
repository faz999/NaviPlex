# PMS plugin framework
from PMS import *
from PMS.Objects import *
from PMS.Shortcuts import *
import re
import urllib
from feed import *

####################################################################################################

VIDEO_PREFIX = "/video/naviplex"
MAIN_URL       = "http://www.navi-x.org/playlists/med_port.plx"
NAME           = L('Title')
CACHE_INTERVAL = 1800
ART            = 'art-default.jpg'
ICON           = 'icon-default.png'
DEBUG          = True

####################################################################################################

def Start():

    Plugin.AddPrefixHandler(VIDEO_PREFIX, VideoMainMenu, L('VideoTitle'), ICON, ART)
    Plugin.AddViewGroup("InfoList", viewMode="InfoList", mediaType="items")
    Plugin.AddViewGroup("List", viewMode="List", mediaType="items")
    MediaContainer.art = R(ART)
    MediaContainer.title1 = NAME
    DirectoryItem.thumb = R(ICON)

def VideoMainMenu():

    dir = MediaContainer(viewGroup="InfoList")
    content = GetContents(MAIN_URL)
    feed = Feed(content)
    for item in feed.items:
      if item.thumb != None:
        thumb = item.thumb
      else:
        thumb = R(ICON)
      dir.Append(
          Function(
            DirectoryItem(
              ReadPage,
              item.name,
              item.description,
              item.description,
              thumb=thumb,
              art=R(ART)
            ),
            url=item.URL
        )
      )

    return dir
    #return ReadPage("", MAIN_URL)


def CallbackExample(sender):

    return MessageContainer(
        "Not implemented",
        "In real life, you'll make more than one callback,\nand you'll do something useful.\nsender.itemTitle=%s" % sender.itemTitle
    )

# ****************************************************
# by wrapping the read for the url, i abstract the method
# which means we can easily switch to the plex framework method
# or use urllib, or whatever.
# ****************************************************
def GetContents(url):
  Log("requesting url: " + url.strip())
  playlist = ""
  try:
    playlist = HTTP.Request(url.strip())
  except:
    Log("error fetching playlist")
  #Log(playlist)
  return playlist

def ReadPage(sender, url):   
    dir = MediaContainer(title2=sender.itemTitle)
    dir.viewGroup = "InfoList"
    content = GetContents(url)    
    #Log("fetched playlist")
    feed = Feed(content)
    Log("loaded feed %s" % feed.title)
    for item in feed.items:
      if item.thumb != None:
        thumb = item.thumb
      else:
        thumb = R(ICON)
      if item.icon!=None:
        art=item.icon
      else:
        art=R(ART)
      Log("thumb = %s" % thumb)
      Log("icon = %s" % thumb)
      dir.Append(
          Function(
            DirectoryItem(
              ReadPage,
              item.name,
              item.description,
              item.description,
              thumb=thumb,
              art=art
            ),
            url=item.URL
        )
      )
    return dir

