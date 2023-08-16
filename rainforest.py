import requests
from typing import Optional

URL = 'https://www.letsrevolutionizetesting.com/challenge'


def make_request(challenge_id=None) -> Optional[str]:
    
    payload = {'format': 'json'}

    if challenge_id:
        # update payload
        payload['id'] = challenge_id

    # make request to domain with challenge_id
    resp = requests.get(URL, payload)

    # extract json output
    json_resp = resp.json()

    # print json response
    print(json_resp)

    # make recursion if there is follow in json_resp
    if 'follow' in json_resp:

        next_challenge_id = json_resp['follow'].split('=')[1]

        # extract follow up request
        return make_request(next_challenge_id)
    
    elif 'message' in json_resp:

        # return message
        return json_resp['message']
    
    return None

if __name__ == '__main__':
    make_request(challenge_id=None)