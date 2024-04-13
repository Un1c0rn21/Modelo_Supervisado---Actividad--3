import csv

pathArchivoCSV='C:/Users/mauri/Desktop/actividad ia/DATASET.csv'

#newline lectura linea a linea
with open(pathArchivoCSV, newline="") as archivo01:

    #Con delimiter definimos la estructura de nuestro archivo, separado por comas 
    #csv.DictReader para diccionarios, csv.reader para listas
    lecturaDeCampos=csv.DictReader(archivo01, delimiter=",")
    
    for RecorridoDeFila in lecturaDeCampos:
        
        print(RecorridoDeFila)

from sklearn import tree

caracteristicas = [[5,3,3,1,12000,13],[3,3,5,1,12000,12],[1,1,1,1,12000,4],[4,2,1,1,12000,8]]
labels = [1,2,3,4]

classifier = tree.DecisionTreeClassifier()
classifier.fit(caracteristicas, labels)
res = classifier.predict([[3,3,5,1,12000,12]])

print(res)