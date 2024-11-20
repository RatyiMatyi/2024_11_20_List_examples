"""
Hozz létre egy listát számokkal, ahol előfordulhatnak duplikációk: [1, 2, 2, 3, 3, 4, 5, 5].
Távolítsd el a duplikált számokat, és írd ki az eredményt!
"""

# lista = [1, 2, 2, 3, 3, 4, 5, 5]
#
# lista.remove(2)
# lista.remove(3)
# lista.remove(5)
# print(lista)
# set-es megoldás

lista = set(lista)
print(lista)