import time

import requests
from bs4 import BeautifulSoup

shindan_url = "https://shindanmaker.com/280267"


def shindan():
    shindan_get = requests.get(shindan_url, headers={"User-Agent": "umabot/1.0.0"})
    soup = BeautifulSoup(shindan_get.text, features="html.parser")

    cookie = shindan_get.cookies
    token = soup.find(id="shindanForm").findChild("input", attrs={"name": "_token"})[
        "value"
    ]

    time.sleep(3)

    shindan_post = requests.post(
        shindan_url,
        data={"_token": token, "shindanName": "wehihi_thihihi"},
        cookies=cookie,
        headers={"User-Agent": "umabot/1.0.0"},
    )
    soup = BeautifulSoup(shindan_post.text, features="html.parser")

    result = soup.find(id="copy-textarea-140")
    return result.text
