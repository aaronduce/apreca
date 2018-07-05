# apreca
# a basic python3 web server
# Written by Aaron Duce 2018
# github.com/aaronduce

from socket import socket
from tkinter import *
import socket
from datetime import datetime

# TkInter GUI Setup and Configuration
hostStartMenuWindow = Tk()
hostStartMenuWindow.geometry("250x400")
hostStartMenuWindow.configure(background='#383838')

logname = "apreca-log.txt"
enteredport = StringVar()
enteredhostfile = StringVar()
status = StringVar()
logtemp = open(logname, "w")
logtemp.write("[" + str(datetime.now()) + "] ALERT: Started logging.")
logtemp.close()

# Socket Definition and Configuration
comm_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def limit(*args):
    value = enteredport.get()
    if len(value) > 5:
        enteredport.set(value[0:5])
        appendLog("ALERT: Character Limit of 5 in enteredport reached - blocked further character.")

def appendLog(tolog):
    log = open(logname, 'a')
    log.write("\n[" + str(datetime.now()) + "] " + tolog)
    log.close()

def setstatus(text, code):
    if code == 0:
        hostStartMenuWindowStatusLabel.configure(foreground="#0F0") # Green
    elif code == 1:
        hostStartMenuWindowStatusLabel.configure(foreground="#FFA500") # Orange
    elif code == 2:
        hostStartMenuWindowStatusLabel.configure(foreground="#F00") # Red
    else:
        hostStartMenuWindowStatusLabel.configure(foreground="#FFF") # White
    status.set(text)

def hoststart():
    host, port = enteredhostfile.get(), enteredport.get()
    if host == "" or port == 0 or host is None:
        setstatus("Host or Port not defined.\nAppended to log: apreca-log.txt", 2)
        appendLog("CRITICAL ERROR: Host or Port not defined.")
    else:
        appendLog("Host and Port defined correctly.")
        comm_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        comm_socket.bind((host, int(port)))
        comm_socket.listen(1)
        setstatus("Running.", 0)

appendLog("Successfully imported modules and created window property.")
appendLog("Successfully defined modules.")

enteredport.trace("w", limit)  # When the enteredport variable changes it runs limit()

# GUI Configuration and Widgets
hostStartMenuWindowAprecaTitle = Label(hostStartMenuWindow, text="apreca", fg="#FFFFFF", font=("Trebuchet MS", 32))
hostStartMenuWindowAprecaTitle.configure(background='#383838')

hostStartMenuWindowAprecaSubTitle = Label(hostStartMenuWindow, text="a basic python3 web server", fg="#FFFFFF", font=("Trebuchet MS", 14))
hostStartMenuWindowAprecaSubTitle.configure(background='#383838')

hostStartMenuWindowAprecaSubSubTitle = Label(hostStartMenuWindow, text="github.com/aaronduce/apreca", fg="#FFFFFF", font=("Trebuchet MS", 10))
hostStartMenuWindowAprecaSubSubTitle.configure(background='#383838')

hostStartMenuWindowPortLabel = Label(hostStartMenuWindow, text="Enter a port number to host \n the server on (max 5 chars)", fg="#FFFFFF", font=("Trebuchet MS", 10))
hostStartMenuWindowPortLabel.configure(background='#383838')
hostStartMenuWindowPortEntry = Entry(hostStartMenuWindow, textvariable=enteredport)

hostStartMenuWindowFileLabel = Label(hostStartMenuWindow, text="Enter a file name to host that \n is in Apreca's directory", fg="#FFFFFF", font=("Trebuchet MS", 10))
hostStartMenuWindowFileLabel.configure(background='#383838')
hostStartMenuWindowFileEntry = Entry(hostStartMenuWindow, textvariable=enteredhostfile)

hostStartMenuWindowStartButton = Button(hostStartMenuWindow, text="Start Host", command=hoststart, bg="#000", fg="#fff", font=("Trebuchet MS", 8))

hostStartMenuWindowStatusLabel = Label(hostStartMenuWindow, text="", textvariable=status, fg="#fff", bg="#383838", font=("Trebuchet MS", 10))

appendLog("Successfully created widgets for GUI.")

# Packs GUI Elements for Window to Display
hostStartMenuWindowAprecaTitle.pack()
hostStartMenuWindowAprecaSubTitle.pack()
hostStartMenuWindowAprecaSubSubTitle.pack()
hostStartMenuWindowPortLabel.pack()
hostStartMenuWindowPortEntry.pack()
hostStartMenuWindowFileLabel.pack()
hostStartMenuWindowFileEntry.pack()
hostStartMenuWindowStartButton.pack()
hostStartMenuWindowStatusLabel.pack()

appendLog("Successfully packed widgets for GUI.")

appendLog("Successfully started GUI.")
hostStartMenuWindow.mainloop()
