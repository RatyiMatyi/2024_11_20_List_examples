# gyümölcsök kiíratása
gyumolcsok = ['alma', 'körte', 'szilva', 'barack']

for gyumolcs in gyumolcsok:
    print(gyumolcs)

print(gyumolcsok)

# hónapok kiíratása
honapok = ['január', 'február','március', 'április', 'május', 'június', 'július'] 

print(honapok)

for honap in honapok:
    print(honap)

# index megjelenítése:
    # 0 január
    # 1 február
honap_index = 1

for honap in honapok:
    print(f"{honap_index} {honap}")
    honap_index += 1

# index felhasználása sorszámok megadásához:
    # 1. január
    # 2. február

honap_index = 1
for honap in honapok:
    print(f"{honap_index} {honap}")
    honap_index += 1