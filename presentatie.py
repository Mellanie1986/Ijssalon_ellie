def Presenteer(dictionary,Totaal, tekst=""):
    #invoer 
    mijn_dict = {'vis' : 10, 'vlees': 25, 'overig' : 15}
    totaal = "€50"
    #uitvoer
    uit = []
    uit.append(tekst)       
    uit.append(len(tekst)*"=")
    for key, value in dictionary.items():
        try:
            uit.append(f"{key} : €{value}")
        except ValueError:
            print(f"Waarde voor {key} is geen geldig getal: {value}")
    
    
    