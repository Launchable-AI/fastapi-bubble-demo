from fastapi import FastAPI
import requests
import os
import json
import random
import logging

import uuid

app = FastAPI()

bubble_api_key = os.environ['bubble_api_key']

@app.post("/mod_users/{data_type}")

def mod_users(data_type: str):
    url = f'https://fastapi-demo.bubbleapps.io/version-test/api/1.1/obj/{data_type}'

    headers = {'Authorization': f'Bearer {bubble_api_key}'}

    r = requests.get(url, headers=headers)

    json_data = r.json()

    for record in json_data['response']['results']:
        _id = record['_id']
        print(f"Processing record: {_id}")

        num = random.randint(1, 9000)
        body = {'uuid': num}

        try:
            r2 = requests.patch(f"{url}/{_id}", data=body, headers=headers)
        except Exception as e:
            return(json.dumps(e))
            logging.info(e)

    return({
        'status': 200,
        'msg': "Updated bubble data"
        })

        # patch to change uuid to random number

    return(r.json())


@app.get("/")
def read_root(email: str):

    # set bubble wf url
    bubble_wf_url = 'https://fastapi-demo.bubbleapps.io/version-test/api/1.1/wf/fastapi_test/'

    identifier = str(uuid.uuid4())
    payload = {'email': email, 'uuid': identifier}
    headers = {'Authorization': f'Bearer {bubble_api_key}'}

    r = requests.post(bubble_wf_url, data=payload, headers=headers)
    return {"Hello": "world"}
~                                                                                                                      
~                               
