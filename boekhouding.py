import csv 
from presentatie import *
from helper import *
mijn_dictionary = {
"Aardbeien_ijs_totaal" : "1000",
"Vanille_ijs_totaal ": "2000",
"Chocolade_ijs_totaal": "1500",
"Waterijsjes_totaal": "750",
}

Totaal_inkomsten = som(mijn_dictionary)
inkomsten = mijn_dictionary
Presenteer(inkomsten , Totaal_inkomsten)
inkomsten = {
    "Aardbeien_ijs_totaal": "1000",
    "Vanille_ijs_totaal": "2000",
    "Chocolade_ijs_totaal": "1500",
    "Waterijsjes_totaal": "750",
}
Totaal_inkomsten = som(inkomsten)
Presenteer(inkomsten, Totaal_inkomsten, "Inkomsten")

with open('boekhouding.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    for key, value in inkomsten.items():
        writer.writerow([key, value])
