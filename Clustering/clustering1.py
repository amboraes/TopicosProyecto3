from operator import itemgetter
dict={}
dicts = []
arrAux = []
x = 0
while x < len(noticias):
  for w in noticias[x][2]:
    if((w in dict) == False):
      dict[w] = 1
    else:
      dict[w] += 1
  output = sorted(dict.items(), key=operator.itemgetter(1),reverse=True)
  if len(output) != 0 and isinstance(noticias[x][0], str):
    if noticias[x][0].isdigit():
      arrAux = [noticias[x][0], output[:5]]
      dicts.append(arrAux)
  dict.clear()
  x += 1
