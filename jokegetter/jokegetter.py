import requests


def get_joke():
    jokeobject = requests.get("https://sv443.net/jokeapi/category/Any?format=json").json()
    if jokeobject["type"] == 'single':
        return jokeobject["joke"]
    else:
        return "- " + jokeobject["setup"] + '\n' + '- ' + jokeobject["delivery"]

if __name__ == '__main__':
    joke = get_joke()
    print(joke)