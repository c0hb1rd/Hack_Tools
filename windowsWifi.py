#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import tkinter
import os
from tkinter import messagebox

class Window():
	def __init__(self, title=None, width=None, height=None):
		self.window = tkinter.Tk(className=title)
		self.window.wm_minsize(width, height)
		self.window.wm_maxsize(width, height)
		self.window.wm_protocol('WM_DELETE_WINDOW', self.handler)

	def mainLoop(self):
		self.window.mainloop()

	def newLabel(self, title=None, x=None, y=None, color=None):
		self.label = tkinter.Label(self.window, text=title, fg=color)
		self.label.place(x=x, y=y)
		return self.label

	def newEntry(self, x=None, y=None):
		self.entry = tkinter.Entry(self.window)
		self.entry.place(x=x, y=y)
		return self.entry

	def newButton(self, title=None, width=None, height=None, x=None, y=None, command=None):
		self.button = tkinter.Button(self.window, text=title, width=width, height=height)
		self.button.place(x=x, y=y)
		return self.button

	def handler(self):
		if messagebox.askokcancel('Quit', 'Do you wanna quit?'):
			cmd(MODE_DISALLOW)
			self.window.quit()


HOSTNAME = 'Hostname'
PASSWORD = 'Password'
WIFI_MANAGER = ' Wifi Manager'
COPYRIGHT = '@CPR : cohbird'
VERSION = 'Version 0.1'
STATE_DISABLE = 'Disable'
STATE_ENABLE = 'Enable'
STATE_START = 'Start'
STATE_STOP = 'Stop'
MODE_ALLOW = 'netsh wlan set hostednetwork mode=allow'
MODE_DISALLOW = 'netsh wlan set hostednetwork mode=disallow'
NETWORK_START = 'netsh wlan start hostednetwork'
cmd = os.system

#init a new window
wd = Window(WIFI_MANAGER, 320, 150)

#TextView and EditView
wd.newLabel(HOSTNAME, 30 + 20, 5)
wd.newLabel(PASSWORD, 30 + 20, 30)
hostnameEntry = wd.newEntry(100 + 20, 5)
passwordEntry = wd.newEntry(100 + 20, 30)

#Application Information View
wd.newLabel(COPYRIGHT, 5, 80 + 20 + 30)
wd.newLabel(VERSION, 245, 80 + 20 + 30)

#ButtonView
setButton = wd.newButton("SET", 5, None, 100, 50 + 10)
onButton = wd.newButton("ON", 5, None, 100 + 50, 50 + 10)
onButton['state'] = 'disabled'
offButton = wd.newButton("OFF", 5, None, 100 + 100, 50 + 10)
offButton['state'] = 'disabled'

#StateView
state = wd.newLabel("State:", 5 + 120, 60 + 40, "black")
stateValue = wd.newLabel(STATE_DISABLE, 40 + 120, 60 + 40, "red")

def getInfo():
	hostname = hostnameEntry.get()
	password = passwordEntry.get()
	if hostname:
		if password:
			if len(password) >= 8:
				message = hostname + password
				messagebox.showinfo('Success', 'OK')

				stateValue['text'] = STATE_ENABLE
				stateValue['fg'] = 'gray'

				onButton['state'] = 'normal'
				offButton['state'] = 'normal'
			else:
				messagebox.showerror("Error", 'Minimum of 8 characters.')
				onButton['state'] = 'disabled'
				offButton['state'] = 'disabled'
				stateValue['text'] = STATE_DISABLE
				stateValue['fg'] = 'red'
		else:
			messagebox.showerror('Error', 'Have not input Password.')
			onButton['state'] = 'disabled'
			offButton['state'] = 'disabled'
			stateValue['text'] = STATE_DISABLE
			stateValue['fg'] = 'red'
	else:
		messagebox.showerror('Error', 'Have not input Hostname')
		onButton['state'] = 'disabled'
		offButton['state'] = 'disabled'
		stateValue['text'] = STATE_DISABLE
		stateValue['fg'] = 'red'

def start():
	hostname = hostnameEntry.get()
	password = passwordEntry.get()
	if hostname:
		if password:
			if len(password) >= 8:
				NETWORK_KEY = 'netsh wlan set hostednetwork key=' + password
				NETWORK_SSID = 'netsh wlan set hostednetwork ssid=' + hostname
				if (not cmd(NETWORK_KEY)) and (not cmd(NETWORK_SSID)) and (not cmd(MODE_ALLOW)) :
					if (not cmd(NETWORK_START)):
						stateValue['text'] = STATE_START
						stateValue['fg'] = 'green'
					else:
						messagebox.showerror('Error', 'Network card have some problem, maybe you can check your device whether up in device manager.')
						onButton['state'] = 'disabled'
						offButton['state'] = 'disabled'
						stateValue['text'] = STATE_DISABLE
						stateValue['fg'] = 'red'
				else:
					messagebox.showerror('Error', 'System have some problem, maybe you can use it on Administrator of root.')
					onButton['state'] = 'disabled'
					offButton['state'] = 'disabled'
					stateValue['text'] = STATE_DISABLE
					stateValue['fg'] = 'red'
				
			else:
				messagebox.showerror("Error", 'Minimum of 8 characters.')
				onButton['state'] = 'disabled'
				offButton['state'] = 'disabled'
				stateValue['text'] = STATE_DISABLE
				stateValue['fg'] = 'red'
		else:
			messagebox.showerror('Error', 'Have not input Password.')
			onButton['state'] = 'disabled'
			offButton['state'] = 'disabled'
			stateValue['text'] = STATE_DISABLE
			stateValue['fg'] = 'red'
	else:
		messagebox.showerror('Error', 'Have not input Hostname')
		onButton['state'] = 'disabled'
		offButton['state'] = 'disabled'
		stateValue['text'] = STATE_DISABLE
		stateValue['fg'] = 'red'
	

def stop():
	if not cmd(MODE_DISALLOW):
		stateValue['text'] = STATE_STOP
		stateValue['fg'] = 'gray'

setButton['command'] = getInfo
onButton['command'] = start
offButton['command'] = stop

wd.mainLoop()
