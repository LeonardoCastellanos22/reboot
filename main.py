from extra.utils import *
import time

def run():
    response_cloudx = login_request_safeuem(user="support", password="G%!9QEkmCENHti")#Login Request
    cookie_safeuem = response_cloudx.cookies.get_dict()['frutossecosreyes-token']
    groups = get_groups_request(cookie_safeuem)
    print(f'Get groups : {groups}')
    group_ids = get_properties_from_groups(groups)
    print(f'Get group id : {group_ids}')
    for group in group_ids :
        devices_to_reboot = get_device_request(cookie_safeuem, group)
        time.sleep(0.5)
        if devices_to_reboot != None:
            device_ids = [device["id"] for device in devices_to_reboot ]
        else :
            continue
        restart_devices = restart_request(device_ids, cookie_safeuem)
        print(f'Devices restarted: {restart_devices}')
        time.sleep(0.5)
    
if __name__ == "__main__":
    run()


