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

        row = [file_name, name_cell, xmin, ymin, xmax, ymax]  # llenamos nuestra lista fila
        dframe.append(row) # añadimos nuestra lista fila a la lista dframe

dataframe = pd.DataFrame(dframe, columns = ["file_name", "name_cell", "xmin","ymin","xmax","ymax"])
dataframe[["file_name", "name_cell", "xmin", "ymin", "xmax", "ymax"]].to_csv('./../Dataset/annotations_blood_cells.csv', index = False) 
