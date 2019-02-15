from ast import literal_eval
import requests
from apiclient import discovery

def __search_images(query, cx_code, key):
    service = discovery.build('customsearch', 'v1', developerKey=key, http=None)
    return service.cse().list(q=query, cx=cx_code, searchType="image", num=1, imgType="photo", safe="off", start=1).execute()

def green_bacon_sandals():
    words = " ".join(literal_eval(requests.get("https://random-word-api.herokuapp.com/word?key=6PEK31B2&number=3").content))
    print("Random words were: '{}'".format(words))
    return __search_images(words, 1, "photo").get("items")[0].get("link")


if __name__ == "__main__":
    print(green_bacon_sandals())

