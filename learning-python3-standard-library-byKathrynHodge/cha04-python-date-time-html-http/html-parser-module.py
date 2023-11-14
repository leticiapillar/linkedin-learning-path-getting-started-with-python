# 05 HTML Parser Module
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        print("Start tag:", tag)
        for attr in attrs:
            print("attr:", attr)
    def handle_endtag(self, tag: str) -> None:
        print("End tag:", tag)
    def handle_comment(self, data: str) -> None:
        print("Comment:", data)
    def handle_data(self, data: str) -> None:
        print("Data:", data)

parser = MyHTMLParser()
parser.feed("<html><head><title>Coder</title></head><body><h1><!--hi-->I am a coder</h1></body></html>")

print()
htmlFile = open("sampleHTML.html", "r")
content = ""
for line in htmlFile:
    content += line
parser.feed(content)

print()
htmlInput = input("Input your HTML: ")
parser.feed(htmlInput)

