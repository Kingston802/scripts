#!/usr/bin/env python3

import gi
gi.require_version('Playerctl', '2.0')
from gi.repository import Playerctl, GLib
from subprocess import Popen

player = Playerctl.Player()
player.last = None 

def on_track_change(player, e):
    # only put notification if title changes ! 
    if player.last != player.get_title():
        track_info = '{artist} - {title}'.format(artist=player.get_artist(), title=player.get_title())
        Popen(['notify-send', track_info])
        player.last = player.get_title() 
        print(track_info)

player.connect('metadata', on_track_change)

GLib.MainLoop().run()
