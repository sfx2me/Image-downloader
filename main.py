import requests
web = input("Paste your website link: ")
r = requests.get(web)

print(r.content)
with open("output.png", "wb") as f:
    f.write(r.content)