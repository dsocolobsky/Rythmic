#!/usr/bin/env python

import sys
import gdata.youtube
import gdata.youtube.service
from subprocess import call

def parseArgs():
    total = ""
    for arg in sys.argv[1:]:
        total += " " + arg 
    return total

def getURL(feed):
    return feed.entry[0].media.player.url

def search(toSearch):
    ytService = gdata.youtube.service.YouTubeService()
    query = gdata.youtube.service.YouTubeVideoQuery()
    query.vq = toSearch
    query.orderby = 'relevance'
    query.racy = 'include'
    feed = ytService.YouTubeQuery(query)
    return getURL(feed)

def callScript(url):
    call(["./youtube-mplayer", url, "8192"])

callScript(search(parseArgs()))
