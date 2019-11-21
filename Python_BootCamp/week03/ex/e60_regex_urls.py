import re
def regex_urls(string_urls):
    if ( len(string_urls) == 0 ):
        return ''
    else:
        Result_urls_list = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string_urls)
        return Result_urls_list
regex_urls('<a href="https://w3resource.com.https://">Python Examples</a><a href="http://github.com">')
