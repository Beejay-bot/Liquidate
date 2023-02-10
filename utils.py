import os
import requests
from dotenv import load_dotenv

load_dotenv()

def deep_loop_json(json_data: dict, includes_mutiple_keys:bool=False):
    array_db = []
    if includes_mutiple_keys is True:
        for key, value in json_data.items():
            if isinstance(json_data[key], dict):
                for i, j in json_data[key].items():
                    array_db.append(i)
        return array_db
    else:
        for key, value in json_data.items():
            for i, j in json_data[key].items():
                array_db.append(i)
        return array_db


def compare_returned_expected_data(
    JsonData1: dict, JsonData2: dict, includes_mutiple_keys: bool = False
) -> bool:
    """
    This function helps to check whether a returned data structure from an API call matches your own expected data/results.
    This is done because fintech service provider are not trustworthy with their response status_codes (Some Fintech provider
     return a 200 status_code for a failed API call or an API that contains error message.)
    ::params Json_data1: Your own mock or expected data structure
    ::params Json_data2: The returned data gotten from an API call/ the returned data.
    ::params includes_mutiple_keys (optional): This is a keyword Argument and expects a boolean value. Should be True if your data
       conatins mutiple key value pairs and at least one of your key value pair is a dictionary. Default value is False
    """
    if (
        isinstance(JsonData2, dict) is not True
        or isinstance(JsonData1, dict) is not True
    ):
        raise "Please make sure you returning the correct data type (dict) for the passed arguments"
    if isinstance(includes_mutiple_keys, bool) is not True:
        raise "kwarg 'includes_mutiple_keys' is not a boolean value"
    jsonData1_keys = deep_loop_json(
        JsonData1, includes_mutiple_keys=includes_mutiple_keys
    )
    jsonData2_keys = deep_loop_json(
        JsonData2, includes_mutiple_keys=includes_mutiple_keys
    )
    check_if_data_exists = [data for data in jsonData1_keys if (data in jsonData2_keys)]
    return bool(check_if_data_exists)


def request_helper(path, request_type, expected_response: dict = None, multiple_keys=False, payload=None):
    """
    :param path:
    :param payload: Parameters passed in for post request
    :param request_type:  POST or GET
    :param expected_response: This is an expected json response if passed
    :return:

    """
    try:
        secret_key = os.getenv('PRIVATE_KEY')
        url = f"{ os.getenv('BASE_URL')}{path}"
        headers = {
            "Accept": "text/plain",
            "AppId":  os.getenv('APP_ID'),
            "Content-Type": "application/json",
            "Authorization": secret_key
        }
        response = requests.request(request_type, url, json=payload, headers=headers)
        if response.status_code == 200 or response.status_code == 201:
            if expected_response:
                if compare_returned_expected_data(
                        response.json(), expected_response,
                        includes_mutiple_keys=multiple_keys):
                    return response.json().get('entity')
                else:
                    return None
            return response.json().get('entity')
    except Exception as a:
        print('ERROR ====>>', a)
    return None