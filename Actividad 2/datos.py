import csv
import pandas as pd

print('Con CSV:')
with open('sp_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            variables = row
            line_count += 1
        else:
            #print(row)
            line_count += 1
 
print('Numero de variables: ' + str(len(row)))
print('Numero de registros: ' + str(line_count-1))
print('Nombre de las columnas: ')
for a in variables:
    print(a)        

print()
print('Con Pandas:')   
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



    # Mostrar el número de variables y el número de registros.
    # Mostrar el nombre de las columnas.
    # Mostrar los tipos de datos.
    
    
    # Selecciones dos columnas que al momento parezcan interesantes. Para ellas:
    #     Mostrar los valores únicos
    #     Mostrar los valores máximos y mínimos
    #     Mostrar la media, la mediana y la desviación estándar.


    


