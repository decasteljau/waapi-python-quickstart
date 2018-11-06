from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint

try:
    # Connecting to Waapi using default URL
    with WaapiClient() as client:

        # Simple RPC
        result = client.call("ak.wwise.core.getInfo")
        pprint(result)

        # RPC with options
        # return an array of all children objects in the default actor-mixer work-unit
        args = {
            "from": {"path": ['\\Actor-Mixer Hierarchy\\Default Work Unit']},
            "transform": [
                {"select": ['children']}
            ]
        }
        options = {
            "return": ['id', 'name','type']
        }
        result = client.call("ak.wwise.core.object.get", args, options=options)
        pprint(result)

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

except CannotConnectToWaapiException:
    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")
