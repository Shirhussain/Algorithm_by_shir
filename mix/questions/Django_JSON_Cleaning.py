# Shir Danishyar
# Django JSON Cleaning
# Imagine you are writing a function within a Django application to parse JSON data.
#  In the Python file, write a program to perform a GET request on the route
#  https://coderbyte.com/api/challenges/json/json-cleaning and then clean the object
#   according to the following rules: Remove all keys that have values of N/A, -, or empty
#   strings. If one of these values appear in an array, remove that single item from the array.
#   Then print the modified object as a string.

# Example Input
# {"name":{"first":"Daniel","middle":"N/A","last":"Smith"},"age":45}

# Example Output
# {"name":{"first":"Daniel","last":"Smith"},"age":45}

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
