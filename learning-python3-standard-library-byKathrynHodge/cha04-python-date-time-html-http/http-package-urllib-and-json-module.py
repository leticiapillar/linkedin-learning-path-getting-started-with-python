# HTTP Package
import urllib.request
import json
import textwrap

# https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224

url = "https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224"
with urllib.request.urlopen(url) as content:
    text = content.read()
    decoded_text = text.decode("utf-8")
    print(textwrap.fill(decoded_text, width=50))

print()

obj = json.loads(decoded_text)
print("get value of 'kind'")
print(obj['kind'])

print()
print("get value of items > 0 > serarchInfo > textSnippet")
print(obj['items'][0]['searchInfo']['textSnippet'])
