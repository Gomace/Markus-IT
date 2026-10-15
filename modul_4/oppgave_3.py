poeng = int(input("Skriv inn antall poeng fra 0-100: "))

if poeng > 100:
    print("Du har litt for mange poeng. Du jukser.")
elif poeng < 0:
    print("Du skylder oss poeng. Gå tilbake på jobb!")
else:
    if poeng >= 90:
        print("A")
    elif poeng >= 80:
        print("B")
    elif poeng >= 60:
        print("C")
    elif poeng >= 50:
        print("D")
    elif poeng >= 40:
        print("E")
    else:
        print("F")

    print("Motsatt rekkefølge:")

    if poeng >= 40:
        print("E")
    elif poeng >= 50:
        print("D")
    elif poeng >= 60:
        print("C")
    elif poeng >= 80:
        print("B")
    elif poeng >= 90:
        print("A")
    else:
        print("F")

# --- Refleksjon ---
# Jeg forventer å få en 'A' når jeg skriver '95', 'C' når jeg skriver '72',
# 'E' når jeg skriver '40', og 'F' når jeg skriver '12'.

# Siden rekkefølgen er snudd, så ville jeg antatt at '95', som er større
# enn eller lik '40' gi utfall 'E'. I henhold til dette så vil nok input
# fra 100 til 40 gi det første utfallet, og lavere gå rett til 'else',
# som er 'F'.

# Det som skjer når du skriver '150' er at du får utfallet 'A', fordi koden
# begrenser ikke hvor høye tall vi kan bruke, og alt som er høyere enn 90
# får 'A'. '-10' gir utfallet 'F' fordi koden setter alt som ikke passer
# innenfor de andre utsagnene til det siste utfallet 'F'.

# Når vi snudde rekkefølgen ble '95' til 'E', fordi 'if poeng >= 40:'
# utsagnet ikke begrenser 'poeng' mengden til '49-40'; siden den vanlige
# rekkefølgen stopper før det utfallet hvis 'poeng' mengden overstrider
# de tallene.

# Forskjellen på flere 'if' etter hverandre, og en 'if/elif' kjede er at
# 'elif' begrenser utfallene til å bli en av mange i listen med utsagn;
# mens mange 'if'er etter hverandre hører bare på om utsagnet er sant,
# urelatert til hva de forrige utsagnene gjorde.

# Grunnen til at vi ikke trenger å sjekke at 'poeng'ene også er under '90'
# på 'B' utfallet er fordi vi vet at sekvensen dekker utfall over '90'
# før den når 'B' utsagnet, og dermed blir sjekken unødvendig.

# 'else' delen kjører bare når alle andre utsagn med 'if' eller 'elif'
# ender opp som 'False'.