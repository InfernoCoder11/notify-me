import subprocess as sub
import argparse
import time
import threading

def Notify(heading, message, minutes = 0):
	seconds = minutes*60
	time.sleep (seconds)
	sub.call(["notify-send", args.heading, args.message])

def AltNotification():
	from PyQt5 import Qt
	import sys
	app = Qt.QApplication(sys.argv)
	systemtray_icon = Qt.QSystemTrayIcon(app)
	systemtray_icon.show()
	systemtray_icon.showMessage('Title', 'Content')

def ParserInit ():
	parser = argparse.ArgumentParser()
	parser.add_argument("heading", help = "Heading of the notification", type = str)
	parser.add_argument("message", help = "Message body of the notification", type = str)
	parser.add_argument("minutes", help = "Notify after how many minutes", type = float)
	args = parser.parse_args()

	return args

if __name__ == "__main__":
	args = ParserInit()
	Thread = threading.Thread(target = Notify, args = (args.heading, args.message, args.minutes, ))
	Thread.start()