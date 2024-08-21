import os
import json
import time
import pytest
import traceback
from helpers.auth_token_helper import get_auth_token


def pytest_addoption(parser) -> None:
    parser.addoption('--env', dest='env', action='store', required=True)
    parser.addoption('--client_id', dest='client_id', action='store')
    parser.addoption('--client_secret', dest='client_secret', action='store')
    parser.addoption('--base_url', dest='base_url', action='store')


def pytest_configuration(config) -> None:
    pytest.env = configure_env(config)

    try:
        os.makedirs(os.getcwd() + os.sep + "Reports")
    except ValueError:
        pass

    current_time = time.strftime("%Y%m%d-%H%M%S")

    try:
        pytest.auth_token = get_auth_token(pytest.env['client_id'], pytest.env['client_secret'], pytest.env['base_url'])
    except Exception() as e:
        raise Exception(traceback.format_exc() + '\n' + 'Unable to get auth token: ' + str(e))


def configure_env(config) -> None:
    env = None
    with open(os.getcwd() + os.sep + 'environment.json', 'r+') as json_file:
        env = json.load(json_file)
        env['env'] = str(config.option.env).lower()

        if config.client_id is not None:
            env['client_id'] = config.option.client_id

        if config.client_id is not None:
            env['client_secret'] = config.option.client_secret

        if config.client_id is not None:
            env['base_url'] = str(config.option.base_url).lower()

        json_file.seek(0)
        json.dump(env, json_file, indent=4)
        json_file.truncate()
        json_file.close()

    return env
