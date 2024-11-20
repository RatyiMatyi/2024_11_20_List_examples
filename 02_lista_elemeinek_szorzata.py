"""
Hozz létre egy listát számokkal: [2, 4, 6, 8]. 
Írd ki a lista elemeinek szorzatát (azaz a számok szorzatát)!
"""

list = [2, 4, 6, 8,]
szorzat = 1
for szam in list:
    szorzat = szam * szorzat
    print(szorzat)