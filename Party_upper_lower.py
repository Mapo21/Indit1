# Party BSP


wetter = input("Wochenendwetter - 'sonnig' oder 'regnerisch': ")
    
# doppeltes '==' Zeichen: Vergleichoperator

if wetter.upper() == "SONNIG":
    print("Gartenparty")
    print("Jippiieeehh")
elif wetter.lower() == "regnerisch":
    print("Kellerparty")
    print("Mist")
else:
    print("bitte entweder 'sonnig' oder 'regnerisch' eingeben!")