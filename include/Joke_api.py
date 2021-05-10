import requests


def get_joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Any")
    if response.json()["type"] == "single":
        print(f"{response.json()['joke']}")
    else:
        print(f"{response.json()['setup']}, {response.json()['delivery']}")
    print("############ re-run code to update ###########")


def get_dark_joke(dark):
    if dark:
        print("Getting a dark joke")
        dark_joke = requests.get("https://v2.jokeapi.dev/joke/Dark")
        if dark_joke.json()["type"] == "single":
            print(dark_joke.json()["joke"])
        else:
            print(f"{dark_joke.json()['setup']}")
            print(f"{dark_joke.json()['delivery']}")
