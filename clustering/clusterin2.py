idNoticia = '195519'
D = {idaux:(contenidoaux) for idaux, contenidoaux in dicts}
palabras = D.get(idNoticia)
dictPal = {}
listaAux = []
for palabra in palabras:
  dictPal[palabra[0]] = None
for ind in dicts:
  if(ind[0] != idNoticia):
    for palabra in palabras:
      for matchs in ind[1]:
        if(palabra[0] in matchs):
          if dictPal[palabra[0]] is None:
            dictPal[palabra[0]] = [[ind[0],matchs[1]]]
          else:
            a = dictPal[palabra[0]]
            b = [ind[0],matchs[1]]
            a.append(b)
            dictPal[palabra[0]]= a

for keys in dictPal:
  tmp = sorted(dictPal[keys], key=lambda x: x[1], reverse = True)
  dictPal[keys] = tmp[:5]
