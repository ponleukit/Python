from datetime import datetime
import requests
import json
def get_currencies(List):
    Collective_list = []
    for i in range(0, len(List)):
        Url = 'https://www.freeforexapi.com/api/live?pairs='+List[i]
        Request = requests.get(Url).json()
        if( Request.get("code",{}) == 200):
            Rate = Request.get("rates",{}).get("{}".format(List[i]),{}).get("rate",{})
            TimeStamp = Request.get("rates",{}).get("{}".format(List[i]),{}).get("timestamp",{})
            Current_time = datetime.fromtimestamp(TimeStamp).strftime("%d/%m/%Y %H:%M:%S")
            Collective_list.append((List[i], Rate, TimeStamp, Current_time))
        else:
            print(Request.get("message"))
            return []
    print(Collective_list)
    return Collective_list
get_currencies(["EURUSD","EURGBP"])
