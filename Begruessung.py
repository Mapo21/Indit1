#Schreiben Sie ein Programm, das in 2 möglichen Versionen, die in der Liste aufgeführten Personen begrüßt
# Z.B.: "Hallo, Peter!"
#
# Version 1: for-Schleife im Hauptprogramm, Ausgabe der Begrüßung in einem Unterprogramm
#
# Version 2: for-Schleife und Ausgabe der Begrüßung in einem Unterprogramm

namen = ["Peter", "Dora", "Kevin", "Fritz", "Sarah"]

def begruessung(name):
    print("Hallo ", name)
    print("Schön dich zu sehen!")
    print("Viel Spaß mit dem Programm!")
    return

def begruessung2(namensliste):
    for ein_name in namensliste:
        print("Hallo ", name, "!")
        print("Schön dich zu sehen!")
        print("Viel Spaß mit dem Programm!")
    return

print("Version 1:")
for name in namen:
    begruessung(name)
    
print("Version 2:")
begruessung2(namen)
