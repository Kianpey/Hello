import requests
from PIL import Image
from io import BytesIO

b = input("code: ")
s = requests.get(f"https://http.cat/{b}.jpg", stream=True)

if s.status_code == 200:
    img = Image.open(BytesIO(s.content))
    img.save(f"{b}.jpg")
else:
    print(f"Error: {s.status_code}")


