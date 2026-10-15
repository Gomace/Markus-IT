aldersgrense = 18
alder = int(input("Hvor gammel er du? "))

if alder > aldersgrense:
    print(f"Du er {alder} år, og gammel nok.")
else:
    print(f"Du er {alder} år, og ikke gammel nok.")

print("Takk for at du sjekket!")

# --- Refleksjon ---
# Før jeg tester med alderene 17, 18, og 19, så forventer jeg at det skal bli
# utfall #2 når jeg skriver 17, og utfall #1 for både 18 og 19.

# Det som skjer når jeg fjerner '=' tegnet fra '>=' er at den ikke inkluderer
# verdien vi sammenligner med, som da er 'aldersgrense', og dermed gir
# utfall #2 i stedet for utfall #1.

# I steg 5 og 6 ble det errorer. Å fjerne innhukket foran 'print()' skapte en
# 'IndentationError', fordi den forventet et inhukk etter 'if' statementet.
# Fjerning av kolonet etter 'if' statementet skapte en 'SyntaxError'. Jeg
# regner med at kolonet forteller Python at den er ferdig med å sjekke etter
# 'boolean' syntax, og er klar til å kjøre kode i en blokk under.

# Linjen fra steg 7 ble skrevet ut uansett fordi den stod utenfor kodeblokkene
# som var begrenset til utfallene av 'if' statementene.

# 'alder >= aldersgrense' git en 'boolean' verdi. Dette er en verdi som enten
# er sann eller usann ('True' eller 'False'). 'if' statements bruker den
# verdien ved å sjekke om den skal utføre en kodeblokk hvis utsagnet er
# 'True', eller hoppe videre til neste, hvis det er noen flere, om det er
# 'False'.

# I utvidelsen er '>=' riktig for en aldersgrense på 18 år, fordi '=' tegnet
# gjør at utsagnet inkluderer verdien den sammenligner med. I dette tilfellet
# '>=' som er større eller lik. Siden aldersgrensen er 18, så vil vi inkludere
# verdien av aldersgrensen i sjekken, så '>' hadde vært feil.
# Dette er en lett feil å gjøre fordi en kan fort tenke på "over 18", og brukte
# tegnet som forteller utsagnet at 'alder' må være større '>' enn 18, når det
# faktiske svaret er "større enn 18, fra og med 18"; som er '>='.