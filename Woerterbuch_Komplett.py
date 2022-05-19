#Ändern Sie das Wörterbuch-Beispiel aus Lab 2 wie folgt:
#
# 1) Verwendung eines od. mehrerer Assoziativ-Arrays (Dictionary)
# 2) Funktion, um übersetzte Begriffe auszulesen
# 3) Funktion, um dem Wörterbuch neue Begriffe hinzuzufügen



mein_woerterbuch = {"apfel":"apple", "birne":"pear", "kirsche":"cherry", "melone":"melon","pfirsich":"peach"}


print("Wählen Sie die gewünschte Funktion: ")
print("Eingabe von [A]: Abfrage")
print("Eingabe von [H]: Eintrag hinzufügen")
    

correct = False
    
while correct == False:        #Schleife bis i.O
    eingabe = input("Funktion eingeben: ")    
    
    if eingabe == "A":
                                        #Funktion zum auslesen
        wort=input("DE Wort eingeben: ") 
        if wort in mein_woerterbuch:
            print("EN Übersetzung: ",mein_woerterbuch[wort]) #Übersetzung
        else:
            print('nicht gefunden')
    elif eingabe == "H":
                                        #Funktion zum hinzufügen
        mein_woerterbuch[input('DE Wort:')] = input('EN Uebersetzung:') 
       
        
    else:
        print("Unbekannte Eingabe")
