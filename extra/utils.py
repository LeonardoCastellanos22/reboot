from . import HEADERS, BASE_URL
import requests

def restart_request(ids_devices, token):
    url = f"{BASE_URL}/api/device/restart"
    body = {"param" : "restart", "ids" : ids_devices,"offline" : False}
    cookies = {"token": token}
    response = create_request(url, HEADERS, "put", data = body, cookies=cookies)
    return response.json()

def get_properties_from_groups(groups):    
    return [group["id"] for group in groups]           
            
def get_groups_request(token):
    url = f"{BASE_URL}/api/deviceGroup/get?deviceCount=false"
    cookies = {"token": token}
    response = requests.get(url, cookies = cookies)    
    return response.json()["groups"]

def get_device_request(token, group):
    url = f"{BASE_URL}/api/device/v2?page=0&size=100&order=asc&by=name&group={group}&until&field=id,name,family,status,deploy,enrollTime,offlineSince,groups,labels,info&filter&session"
    cookies = {"token": token}
    response = requests.get(url, cookies = cookies)
    print(f'Get devices per group ')
    return response.json()["devices"]

def login_request_safeuem(user, password):
    url = f"{BASE_URL}/api/login"
    body = {"username": user, "password": password}
    response = create_request(url, HEADERS, request_type="post", data = body)
    return response


def create_request(url, headers, request_type, data=None, cookies = None):
    """
    Function to make a request to the server
    """
    
    request_func = getattr(requests, request_type)
    kwargs = {"url": url, "headers": headers, "cookies":cookies}
    if request_type == "post" or request_type == "put" or request_type == "delete":
        kwargs["json"] = data
    try:
        req = request_func(**kwargs)
        return req
    except Exception as e:
        print("[ERROR] There was an error with the request, details:")
        print(e)
        
        return None