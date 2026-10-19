riktig_svar = "Oslo"

svar = input("Hva er hovedstaden i Norge? ")

if svar == riktig_svar:
    print("Riktig!")
else:
    print("Feil, svaret var", riktig_svar)

alder = int(input("Hvor gammel er du? "))

if alder == 18:
    print("Du er akkurat myndig!")
else:
    print("Du er ikke 18.")

# --- Refleksjon ---
# Feil #1 og #2 var at 'svar' var '=' lik 'riktig_svar' i 'if' statementen. Riktig syntax hadde
# vært '==', slik at programmet kunne ha sammenlignet verdiene. Det manglet også et kolon
# etter sjekken.

# Feil #3 var at 'else' utfallet i 'svar == riktig_svar' kodeblokken ikke hadde et innhukk, så
# så det kom en error, når det skulle ha skjedd et 'print()' kall.

# Feil #4 og #5 var at 'alder == 18' sjekket om 'alder' verdien var lik tallet '18'. Siden
# brukeren måtte skrive inn alderen selv i en 'input()' kall, var da både 'input()' kallet,
# og 'alder == 18' sjekken like feil, når ingen av dem hadde mulighet til å få eller gi
# daten som var nødvendig i koden.

# Sist så vil jeg kanskje si at det er en feil å sjekke 'alder == 18', men det er ikke sikkert
# dette var en sjekk om de var over '18', eller om de bare var '18' presist.

# Grunnen til at den siste feilen ikke gav en feilmelding, altså feil #4 (regner jeg med), var
# at det ikke var noe feil i koden spesifikt, men heller i oppsettet av koden. Jeg oppdaget den
# da sjekken ikke ville registrere '18' som riktig input, når sjekken tydelig spurte om '18'
# var lik 'alder'.

# Syntaksfeil er når koden ikke er skrevet slik at datamaskinen forstår hva den skal gjøre med
# teksten. Dette gjør at programmet stopper, eller får utforutsette utfall.
# En logisk feil er når koden er korrekt, men oppsettet er feil med tanke på hva det ønskede
# utfallet egentlig skal være. Dette er nok feilen jeg ville sagt var farligst i et vanelig
# program, siden den ikke synes på feilmeldingsvarslene.

# Forstår ikke helt hva spørsmålet er, men fra det jeg forstår så er de verdiene det er lurest
# å teste med for å finne logiske feil i et program som dette: de riktige verdiene. Når du
# skriver inn en forventet verdi, så bør programmet gi forventede resultater. Hvis alt kjører
# slik som det skal etter 2-3 tester, så bør en sjekke med feile verdier.