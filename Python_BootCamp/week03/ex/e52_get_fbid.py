import requests
import re
def Check(response,Status_code):
    Result = []
    try:
        User= re.compile('"entity_id":"([0-9]+)"')
        User_ID = User.findall(str(response.content))
        ID = int(User_ID[0])
        Result.append(Status_code)
        Result.append(ID)
        print(tuple(Result))
        return tuple(Result)
    except:
        Result.append(Status_code)
        Result.append(0)
        print(tuple(Result))
        return tuple(Result)
def get_fbid(Url):
    try:

        response = requests.get(Url)
        Status_code = response.status_code
        Check(response,Status_code)
    except:
        newUrl = 'https://www.facebook.com/' + Url
        response = requests.get(newUrl)
        Status_code = response.status_code
        Check(response,Status_code)
get_fbid("zuck")
