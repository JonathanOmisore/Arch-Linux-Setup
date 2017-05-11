#! /usr/bin/env python3
import webbrowser

file = open("link","r")
link = file.read()
webbrowser.open(link)
