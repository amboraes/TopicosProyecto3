dbutils.widgets.text(name='widget_02', defaultValue='', label = 'Ingrese el id ')
idNoticia = dbutils.widgets.get(name='widget_02')
D = {idaux:(contenidoaux) for idaux, contenidoaux in dicts}
palabras = D.get(idNoticia)
maxim = []
outIds = []
D.pop(idNoticia)
for nots in D:
  acumAux = 0
  lista = D[nots]
  for pal in lista:
    for init in palabras:
      if pal[0] == init[0]:
        acumAux = acumAux + pal[1] + init[1]
        break
  maxim.append([acumAux,nots])

maxim = sorted(maxim, key=lambda x: x[0], reverse = True)
for s in maxim[:5]:
  outIds.append(s[1])
tituloAux = identRowless.index(idNoticia)
taux = title[tituloAux]
titulo = taux[0]
#print(titulo)
#aux2 = ' '.join(outIds)
salida = idNoticia + ", " + titulo + ", "+ str(outIds)
print(salida)
