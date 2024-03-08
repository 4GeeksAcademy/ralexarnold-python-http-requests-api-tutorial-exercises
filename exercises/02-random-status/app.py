import requests

import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/random-status.php")

status_code = str(response.status_code)

print("The response status is: "+str(response.status_code))

if status_code == '404':
    print('The URL you asked is not found')

elif status_code == '503':
    print('Unavailable right now')

elif status_code == '200':
    print('Everything went perfect')

elif status_code == '400':
    print('Something is wrong on the request params')

else:
    print('Anything Else')
