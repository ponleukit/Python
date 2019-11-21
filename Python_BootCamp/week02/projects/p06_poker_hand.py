def poker_hand(P1 , P2):
    CONTAIN_CARD = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
    #player one
    CHECK_FLUSH_P1 = [i[1:]  for i in P1.split()]
    CHECK_CARD_P1 = 0
    CHECK_CARD_P1_I = 0
    CHECK_CARD_P1_II = 0
    P1_WITHOUT_FLUSH = []
    P1_OPPORTUNITY_WIN = 0
    for i in CONTAIN_CARD:
        for j in P1:
            if( i == j):
                P1_WITHOUT_FLUSH.append(j[0:])
    if (len(set(CHECK_FLUSH_P1)) == 1 ):
        for i in range(0, 8):
            for j in range( 0, 5):
                if( P1_WITHOUT_FLUSH[j] == CONTAIN_CARD[j+8]):
                    CHECK_CARD_P1 = CHECK_CARD_P1 + 1
                elif ( P1_WITHOUT_FLUSH[0] == CONTAIN_CARD[i] and P1_WITHOUT_FLUSH[1] == CONTAIN_CARD[i+1] and P1_WITHOUT_FLUSH[2] == CONTAIN_CARD[i+2] and P1_WITHOUT_FLUSH[3] == CONTAIN_CARD[i+3] and P1_WITHOUT_FLUSH[4] == CONTAIN_CARD[i+4]):
                    CHECK_CARD_P1_I = CHECK_CARD_P1_I + 1
        if(CHECK_CARD_P1 == 40):
            P1_OPPORTUNITY_WIN = 10
        elif( CHECK_CARD_P1_I == 5):
            P1_OPPORTUNITY_WIN = 9
        elif ( P1_WITHOUT_FLUSH[0] == "A" and  P1_WITHOUT_FLUSH[1] == "2" and P1_WITHOUT_FLUSH[2] == "3" and  P1_WITHOUT_FLUSH[3] == "4" and P1_WITHOUT_FLUSH[4]=="5"):
            P1_OPPORTUNITY_WIN = 9
        else:
            P1_OPPORTUNITY_WIN = 6
    else:
        if ( len(set(P1_WITHOUT_FLUSH)) == 2):
            if ( P1_WITHOUT_FLUSH[0] == P1_WITHOUT_FLUSH[1] == P1_WITHOUT_FLUSH[2] == P1_WITHOUT_FLUSH[3] or P1_WITHOUT_FLUSH[1] == P1_WITHOUT_FLUSH[2] == P1_WITHOUT_FLUSH[3]==P1_WITHOUT_FLUSH[4]):
                P1_OPPORTUNITY_WIN = 8
            else:
                P1_OPPORTUNITY_WIN = 7
        elif ( len(set(P1_WITHOUT_FLUSH)) == 3):
            if ( P1_WITHOUT_FLUSH[0] == P1_WITHOUT_FLUSH[1] == P1_WITHOUT_FLUSH[2] or P1_WITHOUT_FLUSH[1] == P1_WITHOUT_FLUSH[2] == P1_WITHOUT_FLUSH[3] or P1_WITHOUT_FLUSH[2] == P1_WITHOUT_FLUSH[3] == P1_WITHOUT_FLUSH[4]):
                P1_OPPORTUNITY_WIN = 4
            else:
                P1_OPPORTUNITY_WIN = 3
        elif (len(set(P1_WITHOUT_FLUSH)) == 4 ):
            P1_OPPORTUNITY_WIN = 2
        elif ( len(set(P1_WITHOUT_FLUSH)) == 5):
            for i in range ( 0 , 8):
              if ( P1_WITHOUT_FLUSH[0] == CONTAIN_CARD[i] and P1_WITHOUT_FLUSH[1] == CONTAIN_CARD[i+1] and P1_WITHOUT_FLUSH[2] == CONTAIN_CARD[i+2] and P1_WITHOUT_FLUSH[3] == CONTAIN_CARD[i+3] and P1_WITHOUT_FLUSH[4] == CONTAIN_CARD[i+4]):
                  CHECK_CARD_P1_II = CHECK_CARD_P1_II + 1
            if ( CHECK_CARD_P1_II == 1):
                P1_OPPORTUNITY_WIN = 5
            elif ( P1_WITHOUT_FLUSH[0] == "2" and  P1_WITHOUT_FLUSH[1] == "3" and P1_WITHOUT_FLUSH[2] == "4" and  P1_WITHOUT_FLUSH[3] == "5" and P1_WITHOUT_FLUSH[4]=="A" or P1_WITHOUT_FLUSH[0] == "T" and  P1_WITHOUT_FLUSH[1] == "J" and P1_WITHOUT_FLUSH[2] == "Q" and  P1_WITHOUT_FLUSH[3] == "K" and P1_WITHOUT_FLUSH[4]=="A"):
                P1_OPPORTUNITY_WIN = 5
            else:
                P1_OPPORTUNITY_WIN = 1
        #player two
    CHECK_FLUSH_P2 = [i[1:]  for i in P2.split()]
    CHECK_CARD_P2 = 0
    CHECK_CARD_P2_I = 0
    CHECK_CARD_P2_II = 0
    P2_WITHOUT_FLUSH = []
    P2_OPPORTUNITY_WIN = 0
    for i in CONTAIN_CARD:
        for j in P2:
            if( i == j):
                P2_WITHOUT_FLUSH.append(j[0:])
    if (len(set(CHECK_FLUSH_P2)) == 1 ):
        for i in range(0, 8):
            for j in range( 0, 5):
                if( P2_WITHOUT_FLUSH[j] == CONTAIN_CARD[j+8]):
                    CHECK_CARD_P2 = CHECK_CARD_P2 + 1
                elif ( P2_WITHOUT_FLUSH[0] == CONTAIN_CARD[i] and P2_WITHOUT_FLUSH[1] == CONTAIN_CARD[i+1] and P2_WITHOUT_FLUSH[2] == CONTAIN_CARD[i+2] and P2_WITHOUT_FLUSH[3] == CONTAIN_CARD[i+3] and P2_WITHOUT_FLUSH[4] == CONTAIN_CARD[i+4]):
                    CHECK_CARD_P2_I = CHECK_CARD_P2_I + 1
        if(CHECK_CARD_P2 == 40):
            P2_OPPORTUNITY_WIN = 10
        elif( CHECK_CARD_P2_I == 5):
            P2_OPPORTUNITY_WIN = 9
        elif ( P2_WITHOUT_FLUSH[0] == "A" and  P2_WITHOUT_FLUSH[1] == "2" and P2_WITHOUT_FLUSH[2] == "3" and  P2_WITHOUT_FLUSH[3] == "4" and P2_WITHOUT_FLUSH[4]=="5"):
            P2_OPPORTUNITY_WIN = 9
        else:
            P2_OPPORTUNITY_WIN = 6
    else:
        if ( len(set(P2_WITHOUT_FLUSH)) == 2):
            if ( P2_WITHOUT_FLUSH[0] == P2_WITHOUT_FLUSH[1] == P2_WITHOUT_FLUSH[2] == P2_WITHOUT_FLUSH[3] or P2_WITHOUT_FLUSH[1] == P2_WITHOUT_FLUSH[2] == P2_WITHOUT_FLUSH[3]==P2_WITHOUT_FLUSH[4]):
                P2_OPPORTUNITY_WIN = 8
            else:
                P2_OPPORTUNITY_WIN = 7
        elif ( len(set(P2_WITHOUT_FLUSH)) == 3):
            if ( P2_WITHOUT_FLUSH[0] == P2_WITHOUT_FLUSH[1] == P2_WITHOUT_FLUSH[2] or P2_WITHOUT_FLUSH[1] == P2_WITHOUT_FLUSH[2] == P2_WITHOUT_FLUSH[3] or P2_WITHOUT_FLUSH[2] == P2_WITHOUT_FLUSH[3] == P2_WITHOUT_FLUSH[4]):
                P2_OPPORTUNITY_WIN = 4
            else:
                P2_OPPORTUNITY_WIN = 5
        elif (len(set(P2_WITHOUT_FLUSH)) == 4 ):
            P2_OPPORTUNITY_WIN = 2
        elif ( len(set(P2_WITHOUT_FLUSH)) == 5):
            for i in range( 0, 8):
                if ( P2_WITHOUT_FLUSH[0] == CONTAIN_CARD[i] and P2_WITHOUT_FLUSH[1] == CONTAIN_CARD[i+1] and P2_WITHOUT_FLUSH[2] == CONTAIN_CARD[i+2] and P2_WITHOUT_FLUSH[3] == CONTAIN_CARD[i+3] and P2_WITHOUT_FLUSH[4] == CONTAIN_CARD[i+4]):
                    CHECK_CARD_P2_II = CHECK_CARD_P2_II + 1
            if ( CHECK_CARD_P2_II == 1):
                P2_OPPORTUNITY_WIN = 5
            elif ( P2_WITHOUT_FLUSH[0] == "2" and  P2_WITHOUT_FLUSH[1] == "3" and P2_WITHOUT_FLUSH[2] == "4" and  P2_WITHOUT_FLUSH[3] == "5" and P2_WITHOUT_FLUSH[4]=="A" or P2_WITHOUT_FLUSH[0] == "T" and  P2_WITHOUT_FLUSH[1] == "J" and P2_WITHOUT_FLUSH[2] == "Q" and  P2_WITHOUT_FLUSH[3] == "K" and P2_WITHOUT_FLUSH[4]=="A"):
                P2_OPPORTUNITY_WIN = 5
            else:
                P2_OPPORTUNITY_WIN = 1
    if ( P1_OPPORTUNITY_WIN > P2_OPPORTUNITY_WIN):
        print("P1 WIN")
        return ("P1 WIN")
    elif ( P2_OPPORTUNITY_WIN > P1_OPPORTUNITY_WIN):
        print("P2 WIN")
        return ("P2 WIN")
    else:
        print("TIE")
        return  ("TIE")
poker_hand("AH KS QC JH TH", "AS KH QC JC TC")

