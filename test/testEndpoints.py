import urllib2
# If you are using Python 3+, import urllib instead of urllib2
import json

endpoints = {
    "SitzheizungEndpoint": {
        "url": "https://europewest.services.azureml.net/workspaces/ae27c32fe7da4c589892bda2373629c3/services/9ebbecbd3b9c4ed5a91abb705d8d7ee5/execute?api-version=2.0&details=true",
        "token": "TA/H56aqCju447kv7pjVosZi7/Xz8WkAnP3py+IgyIcpT4dBVWDdgwLL1x1UB1HFWvvz9ICNVsZzWXf5j/i+Mw=="
    },
    "GetriebeEndpoint": {
        "url": "https://europewest.services.azureml.net/workspaces/ae27c32fe7da4c589892bda2373629c3/services/19d165b2e6dc43f886ac75c161fb523f/execute?api-version=2.0&details=true",
        "token": "vajOo8+fd8y6yI5kADEqmRCiwDgSw+YDncek3m3K7QvdCGvyzvOZDXTY7i9T1szhenECzbHl1BCcFoo7lGjEPA=="
    },
    "ElektroEndpoint": {
        "url": "https://europewest.services.azureml.net/workspaces/ae27c32fe7da4c589892bda2373629c3/services/2cd88bb71cd84474b26bcc319fab5c80/execute?api-version=2.0&details=true",
        "token": "jpILvYxeXOf9iy0LvHoIgJkKoYq+4nT8TVGf6nwBmrsFKNQUh+q1Q+NjueQBGlBHifV1d/ueIoWtlEdNeEfdzg=="
    },
    "ColorEndpoint": {
        "url": "https://europewest.services.azureml.net/workspaces/ae27c32fe7da4c589892bda2373629c3/services/1b21057fa8fa466d9f3a299734e977d7/execute?api-version=2.0&details=true",
        "token": "/G02jlz+6eOPytDAzUkf7aqIhAjme1XODIByEoGgvvaWXHOiU2C4KD5MhQpEaO6tdH+5bLtMhQ0y+KTKDX3CiA==",
    },
    "AudioConnectEndpoint": {
        "url": "https://europewest.services.azureml.net/workspaces/ae27c32fe7da4c589892bda2373629c3/services/da4f84e9e98a469f9f3d38585a1fdd30/execute?api-version=2.0&details=true",
        "token": "13t2N7fM1/GgDKqor1IVcYdZj/qnt5r+dIukxZQYsHpV1Ol61oP9/Hloo+dukyo2smP9PRnXdI0cvPhioUCaSg==",
    },
    "AllradEndpoint": {
        "url": "https://europewest.services.azureml.net/workspaces/ae27c32fe7da4c589892bda2373629c3/services/bd75f7d9da9c4759be2c423b31e0b6e2/execute?api-version=2.0&details=true",
        "token": "yW8DGGs6JqA8zVQon6dqUoT4B24UBIe/Z0CG3oh7mYH1Ys+Kboo3CnBKXTahdyaPkyu/WyD8VrlDbBUw5duryA==",
    },
}

data = {
    "Inputs": {
        "input1":
            {
                    "ColumnNames": ["id", "date", "year", "location", "t_m_a3", "t_m_a4", "t_m_a5", "t_m_a6", "t_m_a8", "t_color_gray", "t_color_black", "t_color_white", "t_color_silver", "t_color_blue", "t_g_schalt", "t_g_auto", "t_sitzheizung", "t_connect", "t_allrad", "t_antrieb_e", "modell", "color", "getriebe", "Sitzheizung", "audiconnect", "allrad", "E-antrieb"],
                    "Values": [ [ "0", "value", "0", "value", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "value", "value", "value", "0", "0", "0", "0" ],
                    [ "0", "value", "0", "value", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "value", "value", "value", "0", "0", "0", "0" ], ]
            },
        },
    "GlobalParameters": {}
}

body = str.encode(json.dumps(data))

for name, desc in endpoints.items():
    print("Testing endpoint {}".format(name))

    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ desc["token"])}

    req = urllib2.Request(desc["url"], body, headers)

    try:
        response = urllib2.urlopen(req)

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers)
        # response = urllib.request.urlopen(req)

        result = response.read()
        print(result)
    except urllib2.HTTPError, error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())

        print(json.loads(error.read()))

    print("=====================")