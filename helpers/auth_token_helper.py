import requests
import urllib3


def get_auth_token(client_id: str, client_secret: str, base_url: str):
    urllib3.disable_warnings()

    auth_token_request = requests.post("http://" + base_url + "/login", verify=False,
                                       headers={"Content-Type": "application/json; charset=utf-8"},
                                       json={
                                           "email": client_id,
                                           "password": client_secret
                                       }
                                       )
    json_response = auth_token_request.json()

    return json_response['auth_token']

