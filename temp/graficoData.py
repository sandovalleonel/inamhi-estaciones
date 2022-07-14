from optparse import Values
from typing import Dict
from unicodedata import name
import matplotlib.pyplot as plt
import numpy as np

def limpiarFicheroRamCpu(filename):
    cpu = []
    ramTotal = []
    rasmUsada = []

    with open(filename) as file:
        for line in file:
            lineaString = line.rstrip()
            lineaString = lineaString.replace("  ", " ")
            lineaString = lineaString.replace(",", ".")

            lineaSplit = lineaString.split(" ")

            if(lineaString.find("%Cpu") != -1):
                #print(lineaString.split(" ")[1])
                cpu.append(float(lineaSplit[1]))


            elif(lineaString.find("MiB Mem") != -1):
                rasmUsada.append(float(lineaSplit[10]))
                ramTotal.append(float(lineaSplit[4]))
                #print(lineaSplit[4] +" "+lineaSplit[10])
                #print(lineaString)
    return [cpu,rasmUsada,ramTotal]

def cargarMetricaTiempo(filename):
    tiempos = np.loadtxt(filename,delimiter=",",dtype=float)
    return tiempos


tiempos = cargarMetricaTiempo("tiempo.txt")
tiempos = tiempos*1000

print("tiempos maximo cada modulo ",np.amax(tiempos,axis=0))
tiempos = np.mean(tiempos,axis=0)

print("media de cada modulo ",tiempos)


cpuRam =  limpiarFicheroRamCpu("metricaCPURAM.txt")

cpuDatos = np.array(cpuRam[0])
RamUsada = np.array(cpuRam[1])
RamTotal = np.array(cpuRam[2])

print("Cpu max",np.amax(cpuDatos))
print("Cpu promedio",np.mean(cpuDatos))

print("Ram max",np.amax(RamUsada))
print("Ram proemdio",np.mean(RamUsada))
print("Ram tot",RamTotal[0])




