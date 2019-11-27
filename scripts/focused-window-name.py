#!/usr/bin/python3
import sys

from i3ipc import Connection, Event

i3 = Connection()
focused = i3.get_tree().find_focused()

# remove the if if you want everything printed
if focused.window_instance in ["libreoffice","evince"]:
    print(focused.name,focused.window_class,focused.window_instance)
    print(focused.name[:10])

