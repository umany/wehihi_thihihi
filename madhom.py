import requests
from bs4 import BeautifulSoup

shindan_get = requests.get("https://shindanmaker.com/280267")
soup = BeautifulSoup(shindan_get.text, features="html.parser")

cookie = shindan_get.cookies
token = soup.find(id="shindanForm").findChild("input", attrs={"name": "_token"})[
    "value"
]

shindan_post = requests.post(
    "https://shindanmaker.com/280267",
    data={"_token": token, "shindanName": "wehihi_thihihi"},
    cookies=cookie
)
soup = BeautifulSoup(shindan_post.text, features="html.parser")

result = soup.find(id="copy-textarea-140")

print(result.text)
