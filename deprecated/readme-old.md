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
