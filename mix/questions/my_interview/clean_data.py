# remove the key if it's value contain '', '-', 'N/A'
import requests
import json
url = 'https://coderbyte.com/api/challenges/json/json-cleaning'


def clean_data(url):
    response = requests.get(url)
    # data = dict(response.json())
    data = response.json()

    def remove_invalid(people):
        if isinstance(people, dict):
            keys = list(people.keys())
            for key in keys:
                if people[key] in ['', '-', 'N/A']:
                    del people[key]
                else:
                    remove_invalid(people[key])
        if isinstance(people, list):
            keys = people[:]
            for key in keys:
                if key in ['', '-', 'N/A']:
                    people.remove(key)

    remove_invalid(data)
    return data


print(clean_data(url))
