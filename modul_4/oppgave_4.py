# alder = 25
# er_student = True
# har_medlemskort = False

alder = int(input("Hvor gammel er du? "))
er_student = input("Er du student? (ja/nei) ").lower() == "ja"

barn = 12
pensjonist = 67

pris = 120

if alder <= barn or alder >= 67:
    pris = 0
elif er_student and alder < 30:
    pris = 50
else:
    pris = 120

if er_student and alder >= 30:
    print("Visste du at du ikke fikk rabatt fordi du var gammel?")

if not er_student:
    print("Studenter under 30 får billett til 50 kr!")

print(f"Din pris er: {pris} kr")

# print(alder < 12 or alder > 67) #1
# print(er_student and alder < 30) #2
# print(not har_medlemskort) #3
# print(er_student and har_medlemskort) #4
# print(er_student or har_medlemskort) #5
# print(not er_student or alder < 30) #6

# --- Refleksjon ---
# Jeg antar at 'print()' #1 blir 'False', siden 'alder' ikke er verken mindre enn '12', eller
# mer enn '67'.

# Jeg mener at 'print()' #2 blir 'True' fordi 'er_student' er allerede satt som en 'True'
# 'boolean' verdi, og 'alder' er '25', som er mindre enn '30'.

# Siden 'print()' #3 bruker nøkkelordet 'not', så forandrer 'boolean' verdien seg fra det den
# er til det motsatte. Siden 'har_medlemskort' er satt til 'False', så vil verdien bli snudd
# til 'True'.

# Nå har vi satt inn 2 motsatte 'boolean' verdier i 'print()' #4, og satt nøkkelordet 'and'
# mellom variablene. Det tilsvarer at helheten blir til 'False', siden nøkkelordet 'and'
# krever at begge sidene ender opp å være 'True' for at statementen skal bli ansett som 'True'.

# 'print()' #5 blir 'True' fordi 'or' nøkkelordet krever bare at en av verdiene på sidene er
# 'True'. Siden 'er_student' allerede er 'True', så er en av dem 'True', og dermed hele
# statementen 'True'.

# Siden 'print()' #6 bruker 'or' nøkkelordet, og 'alder' er mindre enn '30', altså '25', så
# er statementen 'True'.

# Det som skjer når brukeren skriver 'Ja' med stor 'J' er at 'string' verdien ikke matcher
# eksakt med det som er tilregnet riktig i variabel 'boolean' sjekk operasjonen.
# Det jeg tror '.lower()' gjør er å forandre 'string' verdien fra brukeren's 'input()' til
# å bli bare små bokstaver. Hvis en bokstav tidligere var stor, så vil den sin lille variant
# erstatte bokstaven.

# 'and' sjekker om to utsagn begge blir sanne før den går videre med å kjøre en kodeblokk,
# mens 'or' sjekker bare om en av utsagnene blir sanne før den går videre.

# Prisen som 35-åringen som var student fikk var 120 kr. Grunnen til dette var at han ikke
# oppfylte kriteriene om studentrabatt, siden de inkluderte at studenten måtte være under
# 30 år gammel.

# Nøkkelordet 'not' bytter en statement sitt 'boolean' value resultat. Hvis en statement
# ble 'True', som (1 + 1 == 2) så vil 'not' gjøre resultatet til 'False'. I samme båt
# ville en 'False' verdi, som (1 + 2 == 1) gitt resultatet 'True' hvis 'not' var skrevet
# før statementen.
# Det er et par måter å skrive steg 4 på uten 'not' nøkkelordet. En av dem hadde vært å
# skrive 'if er_student != True:'. Denne sjekken tester om verdiene på hver side av
# '!=' tegnet ikke matcher, og dermed gjør statementet 'True' hvis det er tilfellet.

# Hvis en 70-åring er student så slår aldersregelen inn først, og overordnet styrer
# prisen til at det blir en gratis billett. Rekkefølgen har mye å si, fordi i en
# 'if/elif' rekke så vil de andre alternativene bli hoppet over hvis en av de øvre
# er sanne. Hvis da 'er_student' hadde vært øverst i rekken, uten 'alder' sjekken,
# så ville 70-åringen ha betalt 50 kr i stedet for å komme inn gratis!