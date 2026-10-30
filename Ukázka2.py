#Výsledek soutěže

# Tuple nelze měnit, musíme použít sorted()
skore_tuple = (15, 82, 43, 99, 61)

# Vytvoříme nový seřazený seznam nejvyšších skóre
top_skore = sorted(skore_tuple, reverse=True)

print("Původní skóre:", skore_tuple)
print("Top skóre (list):", top_skore)