from pypresence import Presence
import handler
import time

client_id = "807964106673225748"
rich_presence = Presence(client_id)

def connect():
    return rich_presence.connect()

def connect_loop(retries=0):
    if retries > 10:
        return
    try:
        connect()
    except:
        print("Where is Discord?")
        time.sleep(10)
        retries += 1
        connect_loop(retries)
    else:
        update_loop()

print("Started Adobe RPC - pcislocked edited")

def update_loop():
    start_time = int(time.time())
    try:
        while True:
            rpc_data = handler.get_rpc_update()
            rich_presence.update(state=rpc_data['state'],
                                 small_image=rpc_data['small_image'],
                                 large_image=rpc_data['large_image'],
                                 large_text=rpc_data['large_text'],
                                 small_text="pcislocked's AdobeRPC",
                                 details=rpc_data['details'],
                                 start=rpc_data['create_time'])
            time.sleep(15) #Reason: https://discord.com/developers/docs/rich-presence/how-to#updating-presence
    except:
        rich_presence.clear()
        print("Exception: I can't find Adobe(maybe?)")
        time.sleep(2)
        update_loop()

try:
    connect_loop()
except KeyboardInterrupt:
    print("Adobe RPC is gone 🦀")
    quit()
