import re
def regex_html(string_args):
    if ( len(string_args) == 0):
        return ''
    else:
        Result_after_regex = re.sub(r'<[^>]*>','', string_args)
        return Result_after_regex
regex_html("<h1>hello</h1> <p>hello</p>")
