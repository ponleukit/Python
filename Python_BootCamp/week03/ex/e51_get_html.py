import urllib.request
def get_html(Url_String):
    try:
        GetUrl = urllib.request.urlopen(Url_String)
        print(GetUrl)
        Result = GetUrl.read().decode()
        return Result
    except:
        return 0
print(get_html('https://www.w3schools.com/'))
