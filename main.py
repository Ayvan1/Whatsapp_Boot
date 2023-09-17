"""
The Programme Whatsapp_boot was created by Ayvan.
The main functions of this programme are as follows
    - search for a contact in your Whatsapp contact
    - Send message and sticker to this contact
    
When you want to send 50 sticker to a friend that is the perfect solution :)
    
"""
from Boot_Whatsapp import Boot
import time
import yaml
def  reader():
    """
    the reader methode reads the yaml config
    Returns:
        _type_: a list of element from the  yaml in Json format
    """
    with open("config.yaml") as file:
        data = yaml.load(file,Loader=yaml.loader.SafeLoader)
        return data
if __name__ == "__main__":
    my_boot = Boot()
    my_boot.wait_load_page()
    input("---> Scan the following QR-code on the Whatsapp page and enter OK: ")
    handling = reader()
    for _ in handling["action"]:
        match _:
            case "name_contact":
                my_boot.search_contact(handling["name_contact"])
            case "msg":
                for msg in handling["msg"]:
                    if msg:
                        my_boot.send_message(msg)
                    else:
                        print(f"---> ... Sir this msg {handling['msg'].index(msg)} is empty")
            case "sticker":
                if handling["sticker"]["sticker_id"] and handling["sticker"]["number_of_items"]:
                    my_boot.send_sticker(index_sticker=handling["sticker"]["sticker_id"],times=handling["sticker"]["number_of_items"])
                else:
                    print("---> ... Sir there are a problem with the info about the sticker")
    time.sleep(5)
    my_boot.boot_end()