import requests
import os
import json


def get_characters():
    request = requests.get(
        url='https://rickandmortyapi.com/api/character', timeout=5)

    if request.status_code == 404:
        print('URL incorrecta')
    elif request.status_code == 200:

        path = os.path.dirname(__file__) + '/data.json'

        with open(path, 'w+') as jsonfile:
            # paste to file
            json.dump(request.json(), jsonfile, indent=4)

            # represent as a json
            # print(json.dumps(request.json()))

            # to python object
            # json.loads(request.json())

            # read a json
            # data = json.load(jsonfile)

            # print(data)


get_characters()
