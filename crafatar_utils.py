from urllib.request import urlopen
from json import loads
from generic_utils import get_dict, get_response

BASE_URL = "https://crafatar.com"

def get_avatars(uuid, **kwargs):
    # build url to fetch data from 
    url = "/".join([BASE_URL, "avatars", uuid])
    # fetch data and convert json to dict
    return url

def get_capes(uuid, **kwargs):
    # build url to fetch data from 
    url = "/".join([BASE_URL, "capes", uuid])
    # fetch data and convert json to dict
    return url

def get_skins(uuid, **kwargs):
    # build url to fetch data from 
    url = "/".join([BASE_URL, "skins", uuid])
    # fetch data and convert json to dict
    return url

def get_head_render(uuid, **kwargs):
    # build url to fetch data from 
    url = "/".join([BASE_URL, "renders/head", uuid])
    # fetch data and convert json to dict
    return url

def get_body_render(uuid, **kwargs):
    # build url to fetch data from 
    url = "/".join([BASE_URL, "renders/body", uuid])
    # fetch data and convert json to dict
    return url
    
