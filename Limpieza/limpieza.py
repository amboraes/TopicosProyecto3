from nltk.corpus import stopwords
import nltk
from re import findall

nltk.download('stopwords')
stop_words = stopwords.words('english')
lines = spark.read.format("csv").option("header","true").option("mode", "DROPMALFORMED").load("dbfs:///FileStore/tables/all-the-news/*.csv")
noticias = []
cantidad = 0
content = lines.select('content').collect()
title = lines.select('title').collect()
ident = lines.select('id').collect()
for x in range(len(content)):
  contentCln = findall(r"[\w']+", str(content[x][0]).lower())
  titleCln = findall(r"[\w']+", str(title[x][0]).lower())
  filtered_Content = [w for w in contentCln if not w in stop_words]
  filtered_Title = [w for w in titleCln if not w in stop_words]
  aux = [ident[x][0],filtered_Title, filtered_Content]
  noticias.append(aux)
