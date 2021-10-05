vraag = input("Is de kaas geel?")
if vraag == 'ja':
    vraag2 = input('Zitten er gaten in?')
    if vraag2 == "ja":
            vraag3 = input("Is de kaas belachelijk duur?")
            if vraag3 == "ja":
                    print("Emmenthaler")
            elif vraag3 == "nee":
                    print("Leerdammer")
    elif vraag2 == 'nee':
        vraag4 = input("Is de kaas hard als steen?")
        if vraag4 == 'ja':
            print("Pamnigiano")
        elif vraag4 == 'nee':
            print("Goude kaas")
if vraag == 'nee':
        vraag5 = input('Heeft de kaas blauwe schimmels')
        if vraag5 == 'nee':
            vraag6 = input("Heeft de kaas een korst?")
            if vraag6 == 'ja':
                print("Camebert")
            elif vraag6 == 'nee':
                print("Foume d'Ambert")
if vraag5 == 'ja':
    vraag7 = input("Heeft de kaas een korst?")
    if vraag7 == 'ja':
            print("Blue de rochbaan")
    elif vraag7 == 'nee':
            print("Foume d'Ambert")
