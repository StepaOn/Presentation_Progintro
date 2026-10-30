# Seřazení slov od nejkratšího po nejdelší


slova = ["slon", "mravenec", "pes", "krokodýl"]

# Předáme funkci len jako klíč
dla_delky = sorted(slova, key=len)

print("Dle délky:", dla_delky)