import pandas as pd

import requests

import shutil

#Utilidad para bajar las fotos de toda la clase a partir de tus listados de alumnos de plumier

datos=pd.read_excel('2BVA.xls', sheet_name='pagina 1')#Sigue el modelo que te sale al bajar el excel con los datos de los alumnos de cada clase en plumierXXI
columna_NRE=datos['NRE'].tolist()
columna_APELLIDO1=datos['APELLIDO 1'].tolist()
columna_APELLIDO2=datos['APELLIDO 2'].tolist()
columna_NOMBRE=datos['NOMBRE'].tolist()
print(datos)
print (columna_NRE)
print (columna_APELLIDO1)
print (columna_APELLIDO2)
print (columna_NOMBRE)

cookie={'JSESSIONID':''}#Aquí tienes que poner tu Jsessión, lo sacas a partir de haberte logeado en tu plumierxxi y darle a la información de las cookies.




for i in range(len(columna_NRE)):
    imagenURL=f"https://profesores.murciaeduca.es/GICWeb/fichaAlumno.ctrl?idAlumno={columna_NRE[i]}&opFicha=FOTO"
    r=requests.get(imagenURL, cookies=cookie, stream=True)
    with open(f'./VA2/{columna_APELLIDO1[i]}-{columna_APELLIDO2[i]}-{columna_NOMBRE[i]}-{columna_NRE[i]}.jpg', 'wb') as f:
        shutil.copyfileobj(r.raw,f)


