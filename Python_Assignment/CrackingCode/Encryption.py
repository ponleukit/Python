def EncrypTion(PlainText, Key):
    Key = Key%25
    CypberText = ""
    for e in PlainText.upper():
        if( 65 <= ord(e) <= 90):
            if( ord(e)+ Key >90):
                CypberText += chr(64 + (ord(e)+Key)%90)
            else:
                CypberText += chr(ord(e) + Key)
        else:
            continue
    return CypberText
print(EncrypTion(input("Enter the plaintext here: "),int(input("Enter the key here: "))))
