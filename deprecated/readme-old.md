## How to use apreca section - MIGRATED TO WIKI

Apreca relies on grabbing the information it presents on the webpage from a text file called ```WebpageContents.txt```, of which you can get a sample copy of from the sample folder in the repo.

The contents of this file can be as simple as just plain text, just like it can be in HTML, but the file must always start with a ```HTTP/1.1 200 OK```.

If the file was to contain:
```
HTTP/1.1 200 OK

Hello, World!
```
it would output ```Hello, World!``` in the client browser.

Expanding on this, just like any other website, you can use HTML tags to style and format the document.

For example, to put the text in a paragraph that will have it's font family as Helvetica, we could use

```<p style="font-family: Helvetica;">Hello, World!</p>```

Or to make the text bold, we could use

```<b>Hello, World!</b>```

## The code

*available in python file in the repo - just look slightly above this markdown

```python
#apreca
#a basic python3 web server
#Written by Aaron Duce 2018
#github.com/aaronduce

import socket

portno = input("Please provide a port number to host on")
HOST, PORT = '', portno

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT

while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request

    file = open("WebpageContents.txt", "r")
    http_response = file.read()
    client_connection.sendall(http_response)
    client_connection.close()
```
