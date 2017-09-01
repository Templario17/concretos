#!/usr/bin/env python 
#-*- coding: utf-8 -*-

from sys import argv
from argparse import ArgumentParser


# Concretos calculo de dosificacion 

# 5 %  desperdicio

# Diccionario dosificacion concreto 

dosificacion = { 3200:[420, 0.67, 0.67, 250],
                 3000:[350, 0.56, 0.84, 184],
                 2500:[300, 0.48, 0.95, 170],
                 2000:[260, 0.63, 0.84, 170],
                 1500:[210, 0.50, 1.00, 160]}

arg = ArgumentParser(
        prog = 'concretos.py',
        version = '1.0',
        description = '''Script para calcular dosificacion de concretos
                         INFORMACION : 
                         Los calculos hechos en esta aplicacion son usados por
                         las constructoras segun norma NR-10,  ''',
        epilog = 'python 2.7 desarrollado por Templario17')

arg.add_argument('-R', '--resistencia', type=int, help='Resistencia del concreto en P.S.I')
arg.add_argument('-T', '--tipo', choices= ['1:2:2', '1:2:3', '1:2:4'],required=False,
             help='Especifica el tipo de concreto')
arg.add_argument('-V', '--volumen', type=int, help='Volumen de la ectructura en Mts 3')

argp = arg.parse_args()
a =  vars(argp)
resis =  a['resistencia']
vol = a['volumen']
tipo = a['tipo']
r = dosificacion[resis]
resultados = []

for a in range(0,4):
    c = float(vol) * r[a]+ (0.05 * float(vol))
    resultados.append(c)

ruta_1 = "plantilla.txt"
ruta_2 = "banner.txt"

def leer_plantilla(ruta_1):
    with open(ruta_1, "r") as f:
        template = f.read()
    return template  


plantilla = leer_plantilla(ruta_1)

def modificar_plantilla(plantilla):
    plantilla_resultados = plantilla.replace('cemento',str(resultados[0]))
    plantilla_resultados = plantilla_resultados.replace('arena', str(resultados[1]))
    plantilla_resultados = plantilla_resultados.replace('grava', str(resultados[2]))
    plantilla_resultados = plantilla_resultados.replace('agua', str(resultados[3]))
    plantilla_resultados = plantilla_resultados.replace('psi', str(resis))
    plantilla_resultados = plantilla_resultados.replace('tipo', str(vol))
    return plantilla_resultados

final = modificar_plantilla(plantilla)

print leer_plantilla(ruta_2)
print final






