dbutils.widgets.text(name='widget_01', defaultValue='', label = 'Ingrese la palabra ')
a = dbutils.widgets.get(name='widget_01')
tempArr = []
arr = []
for y in range(len(noticias)):
  cantidad = noticias[y][1].count(a) + noticias[y][2].count(a)
  if cantidad > 0:
    tempArr = [cantidad, noticias[y][0], title[y][0]]
    arr.append(tempArr)

arr = sorted(arr, key=lambda x: x[0])
arr.reverse()
for z in arr[:10]:
  print(z)
