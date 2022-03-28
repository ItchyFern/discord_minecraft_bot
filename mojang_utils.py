import imp
from multiprocessing.spawn import import_main_path
from urllib.request import urlopen
from json import loads
from generic_utils import get_dict

BASE_URL = "https://api.mojang.com"

def get_uuid(username):
    # build url to fetch data from 
    url = "/".join([BASE_URL, "users/profiles/minecraft", username])
    # fetch data and convert json to dict and get just id from dict
    return get_dict(url)["id"]