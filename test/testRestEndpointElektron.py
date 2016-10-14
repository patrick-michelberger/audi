import urllib2
# If you are using Python 3+, import urllib instead of urllib2
import json


data = {
    "Inputs": {
        "input1":
            {
                    "ColumnNames": ["id", "date", "year", "location", "t_m_a3", "t_m_a4", "t_m_a5", "t_m_a6", "t_m_a8", "t_color_gray", "t_color_black", "t_color_white", "t_color_silver", "t_color_blue", "t_g_schalt", "t_g_auto", "t_sitzheizung", "t_connect", "t_allrad", "t_antrieb_e", "modell", "color", "getriebe", "Sitzheizung", "audiconnect", "allrad", "E-antrieb"],
                    "Values": [ [ "0", "value", "0", "value", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "value", "value", "value", "0", "0", "0", "0" ],
                    [ "0", "value", "0", "value", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "value", "value", "value", "0", "0", "0", "0" ], ]
            },
        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

url = 'https://europewest.services.azureml.net/workspaces/ae27c32fe7da4c589892bda2373629c3/services/e821d80951f744ffb040a8d8ceed2e02/execute?api-version=2.0&details=true'
api_key = '5pt3yXRfffeL6udQTNsZwO07heFoElDX2lUI/MDNokhk5k4TTX/FvXgF51VQEHX2oOg92lszxFyUuEEYBLHAGg==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib2.Request(url, body, headers)

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
