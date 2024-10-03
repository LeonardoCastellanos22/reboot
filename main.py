from extra.utils import *
import time

def run():
    response_cloudx = login_request_safeuem(user="administrator", password="75904268Leo")#Login Request
    cookie_safeuem = response_cloudx.cookies.get_dict()['token']
    groups = get_groups_request(cookie_safeuem)
    group_ids = get_properties_from_groups(groups)
    print(group_ids)
    for group in group_ids :
        devices_to_reboot = get_device_request(cookie_safeuem, group)
        time.sleep(0.5)
        if devices_to_reboot != None:
            device_ids = [device["id"] for device in devices_to_reboot ]
        else :
            continue
        restart_devices = restart_request(device_ids, cookie_safeuem)
        print(restart_devices)
        time.sleep(0.5)

        
        
        
    


    
    
if __name__ == "__main__":
    run()


