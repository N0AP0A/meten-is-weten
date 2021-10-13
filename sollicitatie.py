import sys
niet = "Uw bent niet toegelaten tot de sollicitatie"
naam = input("Wat is uw naam?")
geslacht = input("Welk geslacht bent uw? Man/Vrouw")
praktijk = input(" heeft uw meer dan 4 jaar praktijkervaring met dieren-dressuur OF meer dan 5 jaar ervaring met jongleren OF meer dan 3 jaar praktijkervaring met acrobatiek?")
if praktijk == str.casefold('NEE'):
    print(niet),sys.exit()
diploma = input("Heeft uw bezit van een Diploma MBO-4 ondernemen?")
if diploma == str.casefold('NEE'):
    print(niet),sys.exit()
rijbewijs = input("Heeft uw bezit van een rijbewijs vrachtwagen?")
if rijbewijs == str.casefold('NEE'):
    print(niet),sys.exit()
hoed = input("Heeft uw bezit van een hoge hoed?")
if hoed == str.casefold('NEE'):
    print(niet),sys.exit()
gewicht =int( input ("Wat is uw lichaamsgewicht in kg?"))
if gewicht < 90:
    print(niet),sys.exit()
if geslacht == 'NEE':
    input("Heeft uw een snor breder dan 10cm?")
    if input == str.casefold('NEE'):
        print(niet),sys.exit()
if geslacht == 'JA':
    input("Heeft uw  roodkrulhaar en is langer dan 20cm?")
    if input == str.casefold('NEE'):
        print(niet),sys.exit()
lengte =int( input("Wat is uw lengte in cm?"))
if lengte == str.casefold('NEE'):
    print(niet),sys.exit()
certificaat = input("Heeft uw het certifaact Overleven met gevaarlijk personeel?")
if certificaat == str.casefold('NEE'): 
    print(niet),sys.exit()
elif certificaat == str.casefold("JA"):
    print(f"{naam} jij toegestaan naar deze solicitatie!")
