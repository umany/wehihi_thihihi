from random import randint


def wehihi():
    tweet = ("ｳｪ", "ﾃｨ")[randint(0, 1)]
    i = randint(0, 3)
    text1 = ("ﾋ", "-", "...", "")[i]
    tweet += text1 * randint(1, 20)

    if i == 2:
        tweet += ("ｳｪ", "ﾃｨ")[randint(0, 1)]
    if i in range(1, 3):
        text2 = ("ﾋ", "-")[randint(0, 1)]
        tweet += text2 * randint(1, 20)

    text3 = ("!", "?", "")[randint(0, 2)]
    tweet += text3 * randint(1, 20)

    return tweet
