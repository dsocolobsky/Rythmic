Rythmic
======

This simple CLI application allows you to search for a song and listen to it,
all from your Terminal.

Note this is a **very** early preview, I plan to add a user interface and stuff
like playlists later on. Similar to what Spotify does, but in a much simpler way.

Dependencies
=============
* Python 2.x
* MPLayer
* [youtube-dl](http://rg3.github.io/youtube-dl/)

I use youtube-dl temporarily, until I fix a little issue.

How to use it
===============
Just type `./rythmic.py song title`
So for example, if you want to listen to "Mack the Knife":
`./rythmic.py mack the knife`

After that, you get an mplayer interface, Space pauses and q exits.

You might need to give permission to run the script:
`chmod a+x rythmic.py`
