import requests
from bs4 import BeautifulSoup

shindan_url = "https://shindanmaker.com/280267"


def shindan():
    shindan_get = requests.get(shindan_url)
    soup = BeautifulSoup(shindan_get.text, features="html.parser")

    cookie = shindan_get.cookies
    token = soup.find(id="shindanForm").findChild("input", attrs={"name": "_token"})[
        "value"
    ]

    shindan_post = requests.post(
        shindan_url,
        data={"_token": token, "shindanName": "wehihi_thihihi"},
        cookies=cookie,
    )
    soup = BeautifulSoup(shindan_post.text, features="html.parser")

    result = soup.find(id="copy-textarea-140")
    return result.text
