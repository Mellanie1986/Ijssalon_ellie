from algemene_functies import kopieer

prijs = 4
def aanbieding_1():
    global prijs
prijs = prijs - prijs * 0.1

smaak = "aarbei"
prijs = "4"
korting = "3.60"
mijn_aanbieding = f"vandaag in de aanbieding : emmertje ijs (1 liter) in de smaak {smaak}, van €{prijs} voor €{korting}"
print(mijn_aanbieding)

def inkomsten_btw(a,b,c,d,e,f,g):
    return a+b+c+d+e+f+g
subtotaal = inkomsten_btw(220,430,125,160,205,90,345)
totaal = subtotaal *9 /100
mijn_inkomsten =f"Het totaal van alle inkomsten van deze week is €{subtotaal}, waarover €{totaal} btw betaald dient te worden. "
print(mijn_inkomsten)

a = max(220,430,125,160,205,90,345)
b = min(220,430,125,160,205,90,345)
mijn_lijst =f"{a},{b}"
print(mijn_lijst)

def gemiddelde():
    global gemiddelde
gemiddelde = [220,430,125,160,205,90,345]
lengte = len(gemiddelde)
som = sum (gemiddelde)
totaal = som/lengte
mijn_lijst= f"de gemiddelde inkomsten deze week zijn €{totaal}"
print (mijn_lijst)

def meervoudig():
    global meervoudig
a = max (10,5,3,2,1,2,9)
b = min (10,5,3,2,1,2,9)
mijn_invoerlijst = f"{a},{b}"
print(mijn_invoerlijst)
kopieer("functie")
invoer_lijst_2 = mijn_invoerlijst
def combinatie(invoer_lijst_2):
    return combinatie
print(invoer_lijst_2)

    





