#Nákupní seznam

# Řazení seznamu podle abecedy (A-Z)
nakup = ["Jablka", "Chléb", "Mléko", "Banány"]

print("Původní:", nakup)
nakup.sort()
print("Seřazeno:", nakup)

# Otočení pořadí (Z-A)
nakup.sort(reverse=True)
print("Obráceně:", nakup)

'''
Výstup:
Původní: ['Jablka', 'Chléb', 'Mléko', 'Banány']
Seřazeno: ['Banány', 'Chléb', 'Jablka', 'Mléko']
Obráceně: ['Mléko', 'Jablka', 'Chléb', 'Banány']
'''