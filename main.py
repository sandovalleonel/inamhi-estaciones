import time

from  obtener_datos.ConexionFtp import ConexionFtp
from  paralelismo.ListarArchivos import ListaArchivo
from multiprocessing import Pool

def main():
    """
    url = '/home/leonel/testAuto/M0003/D1/2020/12/02'
    url = ''
    destino_descarga = ""
    primera_con = ConexionFtp("172.16.183.128","leonel","23456789",url ,destino_descarga)
    primera_con.connn()
    """
    linkRutas = ['/home/leonel/Documentos/tesis/testAuto/M0003/D1/2014/11/28',
                 '/home/leonel/Documentos/tesis/testAuto/M0003/D1/2014/11/28',
                 '/home/leonel/Documentos/tesis/testAuto/M0003/D1/2014/11/28',
                 '/home/leonel/Documentos/tesis/testAuto/M0003/D1/2014/11/28',
                 '/home/leonel/Documentos/tesis/testAuto/M0003/D1/2014/11/28',
                 '/home/leonel/Documentos/tesis/testAuto/M0003/D1/2014/11/28',
                 '/home/leonel/Documentos/tesis/testAuto/M0003/D1/2014/11/28',
                 '/home/leonel/Documentos/tesis/testAuto/M0003/D1/2014/11/28',
                 '/home/leonel/Documentos/tesis/testAuto/M0003/D1/2014/11/28',
                 '/home/leonel/Documentos/tesis/testAuto/M0003/D1/2014/11/28',
                 '/home/leonel/Documentos/tesis/testAuto/M0003/D1/2014/11/28',
                 '/home/leonel/Documentos/tesis/testAuto/M0003/D1/2014/11/28',
                 '/home/leonel/Documentos/tesis/testAuto/M0003/D1/2014/11/28',
                 '/home/leonel/Documentos/tesis/testAuto/M0003/D1/2014/11/28',
                 '/home/leonel/Documentos/tesis/testAuto/M0003/D1/2014/11/28',
                 '/home/leonel/Documentos/tesis/testAuto/M0003/D1/2014/11/28',
                 '/home/leonel/Documentos/tesis/testAuto/M0003/D1/2014/11/28',
                 '/home/leonel/Documentos/tesis/testAuto/M0003/D1/2014/11/28',
                 '/home/leonel/Documentos/tesis/testAuto/M0003/D1/2014/11/28',
                 '/home/leonel/Documentos/tesis/testAuto/M0003/D1/2014/11/28',
                 '/home/leonel/Documentos/tesis/testAuto/M0003/D1/2014/11/28',
                 '/home/leonel/Documentos/tesis/testAuto/M0003/D1/2014/11/28',
                 '/home/leonel/Documentos/tesis/testAuto/M0003/D1/2014/11/28',
                 '/home/leonel/Documentos/tesis/testAuto/M0003/D1/2014/11/28'
                 ]
    listaArchivo = ListaArchivo()
    tiempoInicio = time.time()
    for ruta in linkRutas:
        listaArchivo.imprimirArchivos(ruta)
    tiempoFin = time.time()
    print("-"*15,"timepo" ,(tiempoFin-tiempoInicio))

    tiempoInicio = time.time()
    with Pool(24) as p:
        p.map(listaArchivo.imprimirArchivos, linkRutas)
    tiempoFin = time.time()
    print("-" * 15, "timepo", (tiempoFin - tiempoInicio))



if __name__ == "__main__":
    main()

