from waapi import WaapiClient

# Connect (default URL)
client = WaapiClient()

# Simple RPC
result = client.call("ak.wwise.core.getInfo")
print(result)

# RPC with options
# return an array of all objects in the default actor-mixer work-unit
args = {
    "from": {"path": ['\\Actor-Mixer Hierarchy']},
    "transform": [
        {"select": ['children']}
    ]
}
options = {
    "return": ['id', 'name','type']
}
result = client.call("ak.wwise.core.object.get", args, options=options)
print(result)

# Subscribe
handler = client.subscribe(
    "ak.wwise.core.object.created",
    lambda object: print("Object created: " + str(object))
)

# Bind a different callback at any time
def my_callback(object):
    print("Different callback: " + str(object))

handler.bind(my_callback)

# Unsubscribe
handler.unsubscribe()

# Disconnect
client.disconnect()
