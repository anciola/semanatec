#import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.cluster import KMeans

# print('Con CSV:')
# with open('sp_data.csv') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             variables = row
#             line_count += 1
#         else:
#             #print(row)
#             line_count += 1
 
# print('Numero de variables: ' + str(len(row)))
# print('Numero de registros: ' + str(line_count-1))
# print('Nombre de las columnas: ')
# for a in variables:
#     print(a)        

# print()
# print('Con Pandas:')   
df = pd.read_csv('sp_data.csv')
print('Numero de variables: ' + str(df.shape[1]))
print('Numero de registros: ' + str(df.shape[0]))
print('Nombre de las columnas: ')
print(df.columns)
print('Tipo de los datos: ')
print(df.dtypes)

print()
print("Estadisticas de la columna 'duration_ms'")
print("hay", len(df["duration_ms"].unique()),"diferentes duraciones")
print("la maxima fue", df["duration_ms"].max()/60000)
print("la minima fue", df["duration_ms"].min()/60000)
print("la media fue", df["duration_ms"].mean()/60000)
print("la mediana fue", df["duration_ms"].median()/60000)
print("la desviacion estandar fue de", df["duration_ms"].std()/60000)

print()
print("Estadisticas de la columna 'tempo'")
print("hay", len(df["tempo"].unique()),"diferentes tempos")
print("la maxima fue",df["tempo"].max())
print("la minima fue", df["tempo"].min())
print("la media fue", df["tempo"].mean())
print("la mediana fue",df["tempo"].median())
print("la desviacion estandar fue de",df["tempo"].std())


bins = np.arange(0, df.duration_ms.max()+1.5)-0.5
bins = np.arange(0, 5 +1.5)-0.5
df.hist(column= "duration_ms")
plt.show()
df.boxplot(column= "duration_ms")
plt.show()
    
bins = np.arange(0, df.tempo.max()+1.5)-0.5
bins = np.arange(0, 5 +1.5)-0.5
df.hist(column= "tempo")
plt.show()
df.boxplot(column= "tempo")
plt.show()

print(df.corr())

plt.figure(figsize=(15,5))
sns.heatmap(df.corr())
plt.show()

plt.figure(figsize=(15,5))
column = df.corr()[["liked"]].sort_values(by="liked", ascending = False)
sns.heatmap(column, vmin=-1, vmax=1, annot=True)
plt.show()

test = df[["energy","danceability"]]
test = test.dropna(axis=0, how = 'any')

kmeans = KMeans(n_clusters=3).fit(test)
centroids = kmeans.cluster_centers_
print(centroids)
cla = kmeans.predict(test)


plt.scatter(df["energy"],df["danceability"],c=cla)
for i in range(len(centroids)):
    plt.scatter(centroids[i][0], centroids[i][1], marker="*",c="red")
plt.ylabel("danceability")
plt.xlabel("energy")
plt.show()
