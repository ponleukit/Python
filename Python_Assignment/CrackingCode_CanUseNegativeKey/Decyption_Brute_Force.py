def Check_Condition(CyberText,PossibleKey,PlainText):
    for c in CyberText.upper():
        if ( 65 <= ord(c) <=90):
            if (ord(c) - PossibleKey < 65):
                PlainText += chr(91 - 65%(ord(c) - PossibleKey))
            else:
                PlainText += chr(ord(c) - PossibleKey)
        else:
            continue
    print("key:" + str(PossibleKey) + " " + PlainText )
def FindResult(CyberText,PossibleKey):
    if(PossibleKey == 1):
        PlainText = ""
        Check_Condition(CyberText,PossibleKey,PlainText)
        return PlainText
    else:
        PlainText =""
        Check_Condition(CyberText,PossibleKey,PlainText)
        return FindResult(CyberText, PossibleKey - 1)

def Decryption_BruteForce(CyberText):
    PossibleKey = 25
    PlainText = FindResult(CyberText,PossibleKey)
    print(PlainText)
Decryption_BruteForce(input("Enter the CyberText here: "))
