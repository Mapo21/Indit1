# Aufgabe: Wörterbuch DE -> EN
# Kurzes Programm das nach Eingabe des deutschen Begriffs die englische Übersetzung ausgibt,
# bzw. falls nicht im Wörterbuch zu finden ist eine entsprechende Meldung

#Aufgabe:
#Erweitern und ändern Sie das vorhandene Wörterbuch-Beispiel unter Verwendung eines Dictionarys

#Dictionary:
mein_woerterbuch = {"apfel":"apple", "birne":"pear", "kirsche":"cherry", "melone":"melon","pfirsich":"peach"}

eingabe = input("Eingabe deutsches Wort: ")
eingabe = eingabe.lower() #Umwandlung Kleinbuchstaben

if eingabe not in mein_woerterbuch: #ueberpruefen ob wort in woerterbuch
    print("Wort nicht vorhanden") #Meldung
    
else:
    print("Englisches Wort:  ", mein_woerterbuch[eingabe]) #Übersetzung  
