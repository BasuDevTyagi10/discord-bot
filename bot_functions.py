SWEAR_WORDS = list()

file = open('./data/swear_words.txt', 'r')
for word in file:
    SWEAR_WORDS.append(word.strip())

def getTopicInfo(topic):
    import wikipedia
    return wikipedia.summary(topic,sentences=2)

def getMemeURL():
    import requests
    res = requests.get('https://some-random-api.ml/meme')
    return res.json()['image']