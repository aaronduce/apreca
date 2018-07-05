#apreca
#a basic python3 web server
#Written by Aaron Duce 2018
#github.com/aaronduce

from tkinter import *
import socket

hostStartMenuWindow = Tk()
hostStartMenuWindow.geometry("250x400")
hostStartMenuWindow.configure(background='#383838')

def limit(*args):
    value = enteredport.get()
    if len(value) > 5:
        enteredport.set(value[0:5])

def hostStart():
    print("")

enteredport = StringVar()
enteredhostfile = StringVar()

enteredport.trace("w", limit)

hostStartMenuWindowAprecaTitle = Label(hostStartMenuWindow, text = "apreca", fg="#FFFFFF", font=("Trebuchet MS", 32))
hostStartMenuWindowAprecaTitle.configure(background='#383838')

hostStartMenuWindowAprecaSubTitle = Label(hostStartMenuWindow, text = "a basic python3 web server", fg="#FFFFFF", font=("Trebuchet MS", 14))
hostStartMenuWindowAprecaSubTitle.configure(background='#383838')

hostStartMenuWindowAprecaSubSubTitle = Label(hostStartMenuWindow, text = "github.com/aaronduce/apreca", fg="#FFFFFF", font=("Trebuchet MS", 10))
hostStartMenuWindowAprecaSubSubTitle.configure(background='#383838')

hostStartMenuWindowPortLabel = Label(hostStartMenuWindow, text = "Enter a port number to host \n the server on (max 5 chars)", fg="#FFFFFF", font=("Trebuchet MS", 10))
hostStartMenuWindowPortLabel.configure(background='#383838')
hostStartMenuWindowPortEntry = Entry(hostStartMenuWindow, textvariable = enteredport)

hostStartMenuWindowFileLabel = Label(hostStartMenuWindow, text = "Enter a file name to host that \n is in Apreca's directory", fg="#FFFFFF", font=("Trebuchet MS", 10))
hostStartMenuWindowFileLabel.configure(background='#383838')
hostStartMenuWindowFileEntry = Entry(hostStartMenuWindow, textvariable = enteredhostfile, pady = 10)

hostStartMenuWindowStartButton = Button(hostStartMenuWindow, text = "Start Host", command = hostStart, bg="#000", fg="#fff", font=("Trebuchet MS", 8))

hostStartMenuWindowAprecaTitle.pack()
hostStartMenuWindowAprecaSubTitle.pack()
hostStartMenuWindowAprecaSubSubTitle.pack()
hostStartMenuWindowPortLabel.pack()
hostStartMenuWindowPortEntry.pack()
hostStartMenuWindowFileLabel.pack()
hostStartMenuWindowFileEntry.pack()
hostStartMenuWindowStartButton.pack()



hostStartMenuWindow.mainloop()

def setupSocket():
    if enteredport.get() != None:
        HOST, PORT = '', int(enteredport.get())
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_socket.bind((HOST, PORT))
        listen_socket.listen(1)
    else:
        setupSocket()

setupSocket()

##while True:
##    client_connection, client_address = listen_socket.accept()
##    request = client_connection.recv(1024)
##    print request
##
##    file = open("WebpageContents.txt", "r")
##    http_response = file.read()
##    client_connection.sendall(http_response)
##    client_connection.close()
