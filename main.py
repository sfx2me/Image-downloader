import requests
image_url = input("Paste image url: ")
r = requests.get(image_url)
filename = image_url.split("/")[-1]
with open(filename, "wb") as f:
    f.write(r.content)
print(f"Saved image {file_name}")
