#apreca
#a basic python3 web server
#Written by Aaron Duce 2018
#github.com/aaronduce

from tkinter import *
import tkFont
import socket

defaultFont = Font(family="Helvetica",size=36,weight="bold")

hostStartMenuWindow = Tk()
hostStartMenuWindow.geometry("250x150")
hostStartMenuWindow.configure(background='#383838')

hostStartMenuWindowAprecaTitle = Label(hostStartMenuWindow, text = "Register a new user using the form:", fg="#FFFFFF")
hostStartMenuWindowAprecaTitle.configure(background='#383838')

hostStartMenuWindowAprecaTitle.pack()

hostStartMenuWindow.mainloop()
###portno = input("Please provide a port number to host on")
###HOST, PORT = '', portno

##listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
##listen_socket.bind((HOST, PORT))
##listen_socket.listen(1)
##print 'Serving HTTP on port %s ...' % PORT
##
##while True:
##    client_connection, client_address = listen_socket.accept()
##    request = client_connection.recv(1024)
##    print request
##
##    file = open("WebpageContents.txt", "r")
##    http_response = file.read()
##    client_connection.sendall(http_response)
##    client_connection.close()
