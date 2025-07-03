def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()
    
def fooi_pp(bedrag, personen):
    try: 
        bedrag_pp = bedrag/personen
    except:
        bedrag_pp ="??"
        return f"Het bedrag per persoon is €{bedrag_pp}"
    
def onderstreept(tekst=" "):
    uit = []
    uit.append(tekst)    
    uit.append(len(tekst)*"=")
    return uit

def som(dictionary):
    totaal = 0
    for key, value in dictionary.items():
        try:
            totaal += int(value)
        except ValueError:
            print(f"Waarde voor {key} is geen geldig getal: {value}")
    return totaal
