#DATA MANAGE

import pandas as pd
import os
import xml.etree.ElementTree as ET
from glob import glob

'''
Programa para creación del documento CSV requerido en data_viz.py
'''

annotations = sorted(glob('./../Dataset/BCCD/Annotations/*.xml'))   # importamos el dataset de las anotaciones XML
dframe=[]

print("Cantidad leída: {} archivos".format(len(annotations)))
label_f = lambda x: 0 if x=='RBC' else (1 if x=='WBC' else 2) # asignamos enteros a las 3 posibles etiquetas 

# Dimensiones de las imágenes del Dataset
img_width = 640
img_height = 480

for file in annotations: # para recorrer la carpeta Annotations con los XML respectivos
   
    file_name = file.split('/')[-1].split('\\')[-1].split('.')[0] + '.jpg' # '\' corregido para windows
    tree = ET.parse(file)
    root = tree.getroot().iter('object')
    row = []

    for node in root: # buscamos en cada .XML los parámetros requeridos

        name_cell = node.find('name').text 
        xmin = int(node.find("bndbox/xmin").text)
        ymin = int(node.find("bndbox/ymin").text)
        xmax = int(node.find("bndbox/xmax").text)
        ymax = int(node.find("bndbox/ymax").text)

        # 'round' redondea el flotante a precisión 5
        width_norm = round(float((xmax - xmin)/img_width), 5)    # anchura normalizada [0, 1]
        height_norm = round(float((ymax - ymin)/img_height), 5)    # altura normalizada [0, 1]
        x_center_norm = round(float ((xmin/img_width) + (width_norm/2.)), 5) # normalizamos el xmin para sumar con with_norm/2 y hallar centroide X 
        y_center_norm = round(float((ymin/img_height) + (height_norm/2.)), 5) # normalizamos el ymin para sumar con height_norm/2 y hallar centroide Y 


        label = int(label_f(name_cell))  # usamos la función anónima para asignar una etiqueta a la clase

        row = [file_name, name_cell, label, xmin, ymin, xmax, ymax, width_norm, height_norm, x_center_norm, y_center_norm]  # llenamos nuestra lista fila
        dframe.append(row) # añadimos nuestra lista fila a la lista dframe

dataframe = pd.DataFrame(dframe, columns = ["file_name", "name_cell", "label", "xmin", "ymin", "xmax", "ymax", "width_norm", "height_norm", "x_center_norm", "y_center_norm"])
dataframe[["file_name", "name_cell", "label", "xmin", "ymin", "xmax", "ymax", "width_norm", "height_norm", "x_center_norm", "y_center_norm"]].to_csv('./../Dataset/annotations_blood_cells.csv', index = False)
