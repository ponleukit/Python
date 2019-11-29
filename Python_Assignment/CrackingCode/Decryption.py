def Decryption(CyberText, Key):
    Key = Key%25
    PlainText = ""
    for c in CyberText.upper():
        if (65 <= ord(c)  <= 90):
            if (ord(c) - Key < 65 ):
                PlainText += chr(91 - 65%(ord(c) - Key))
            else:
                PlainText += chr(ord(c) - Key)
        else:
            continue
    return PlainText
print(Decryption(input("Enter the CyberText here: "), int(input("Insert the Key here: "))))
