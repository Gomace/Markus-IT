navn = input("Hva heter du? ")

alder = input("Hvor gammel er du? ")
print(type(alder))
alder = int(alder)
print(type(alder))

height = float(input("Hvor høy er du i meter? "))
print(type(height))

print("Hei,", navn)
print(f"Hei, {navn}!")
print(f"Du blir {alder + 1} til neste år!")
print(f"Din høyde er {height}m!")

# --- Refleksjon ---
# Det som skjer når jeg bruker 'int()' på 'height' er at brukere ender
# opp med å ofte skrive høyde i desimaltall basert på meter. Dette
# forårsaker at variablen endrer 'type' til 'float'.

# 'type()' svarte at 'alder' var en 'str', altså en 'string' før jeg
# brukte 'int()' på den. 'input()' gir meg 'string' datatypen fordi
# den forhåndsprogrammerte verdien til 'input()' er 'string'. Det er
# nok lettere å ta imot brukerskrevet input som 'string' siden det
# gir rom for mye flere tegn.

# Python klagde på i steg 5 at den ikke kunne "concatenate" 'int',
# bare 'string' verdier. Dette tilsvarer at flere 'string' verdier
# kan spleises sammen. Dette var ikke mulig med en annen datatype
# enn 'string'. Kanskje fordi 'int' verdier som '+'es sammen blir
# til utregninger i stedet for sammenspleisinger.

# Etter å ha sammenlignet 'print("Hei,", navn)' med 'print(f"Hei, {navn}!")'
# så mener jeg at 'f-strengen' er lettere å lese. Ettersom ',' etter 'string'
# verdien også legger til et mellomrom, så blir det mer oversiktlig hva
# 'print()' outputen ender opp med å være når vi bruker 'f-string'er.

# Det som skjer når brukeren skriver 'tretti' i stedet for '30' er at vi får
# en error som beskriver at det er en
# 'invalid literal for int() with base 10: 'tretti''
# Dette forteller meg at inputen forventet en 'int'-klar 'string', i stedet
# for en faktisk 'string'.