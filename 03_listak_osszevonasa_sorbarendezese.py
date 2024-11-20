"""
Hozz létre két listát: [3, 1, 4] és [9, 7, 2]. 
Egyesítsd a két listát, és rendezd a lista elemeit növekvő sorrendbe!
"""
lista1 = [3, 1, 4]
lista2 = [9, 7, 2]

nlist = lista1 + lista2
nlist.sort()
print(nlist)
# írasd ki az első és az utolsó elemet!

print(nlist[0], nlist[-1])
