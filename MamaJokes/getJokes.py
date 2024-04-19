import json
import random

def getJoke():
    json_file_path = r'C:\Users\jabbe\PycharmProjects\GithubPush\siegeAPI\jokes.json'

    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        sentences = json.load(json_file)
    return random.choice(sentences)