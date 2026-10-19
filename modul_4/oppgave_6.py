riktig_brukernavn = "michael"
riktig_passord = "python123"
aldersgrense = 13

brukernavn = input("Skriv inn brukernavn: ")
passord = input("Skriv inn passord: ")
alder = int(input("Skriv inn din alder: "))

if alder < aldersgrense:
    print("Du er for ung til å logge inn!")
elif brukernavn == riktig_brukernavn:
    if passord == riktig_passord:
        print(f"Velkommen, {riktig_brukernavn}!")
    elif passord != riktig_passord:
        print("Feil passord.")
else:
    print("Ukjent bruker.")

# --- Refleksjon ---
# Det jeg forventer fra å skrive:
# - "riktig brukernavn, riktig passord" er at utfallet blir 'Velkommen, michael!'
# - "riktig brukernavn, feil passord" er at utfallet blir 'Feil passord.'.
# - både "feil brukernavn, riktig passord" og "feil brukernavn, feil passord" er 'Ukjent bruker.'.

# Jeg brukte ikke 'and' ettersom jeg anså koden som litt mindre "clean" med den tilnærmingen. I
# stedet så brukte jeg nested 'if' statements for å bygge koden med litt mere kontroll i tankene.
# Det finnes flere måter å løse oppgaven på. Det hadde vært mulig å bruke 'not' i stedet for '!=',
# og 'and' på repetisjon hvis jeg ikke hadde sjekket 'brukernavn == riktig_brukernavn' eller
# 'alder < aldersgrense' på en egne 'if'-statements.

# Sjekkene måtte stå i rekkefølge av:
# 1. alder
# 2. brukernavn
# 3. passord
# 4. Ukjen bruker
# Grunnen til dette er at 'alder' skal hoppe rett til mangelen på tilgang. Brukernavnet skal diktere
# om brukeren skal få en av to alternativ, eller om den skal til 'Ukjent bruker', og passord dikterer
# om du har gjort en full success eller bommet. Hadde rekkefølgen blitt endret så måtte vi ha satt
# inn mange flere sjekker for å få de samme utfallene, og da hadde vi repetert veldig mye kode.

# Jeg tror at ekte nettsider skriver "Feil brukernavn eller passord" for å hindre folk i fra å gjette
# seg inn på kontoer som ikke er deres med hint om at du er på ritkig retning med passord eller
# brukernavn.

# Det er viktig å teste alle fire kombinasjonene fordi det kan være noe galt med kode logikken, og ikke
# nødvendigvis bare kode syntaksen. Når kode logikken er feil, så vil utfallene bli veldig annerledes
# enn det vi forventer, selv når brukeren gjør de riktige valgene.