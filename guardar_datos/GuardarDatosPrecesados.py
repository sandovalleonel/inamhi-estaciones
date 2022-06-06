import psycopg2

def guardar(lista,nombreEstacion,nombreFichero):
    #print(nombreFichero.split("_")[-1])
    obtenerInformacionFecha(nombreFichero)
    nombreEstacion = nombreEstacion.split(".")[0]
    lista_Guardar = []
    print("guardando estacion" + nombreEstacion)
    for val in lista:
        insertarTablas = (f"insert into test.{nombreEstacion}_{val[0].split('_')[1]} (nom,res,tot)values('{val[0]}','{val[1]}','{val[2]}');")
        lista_Guardar.append(insertarTablas)
    crearConexionYGuardar(lista_Guardar)
    ###########guardar
    obtenerUltimoRegistro()



def crearConexionYGuardar(listaSql):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="admin",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="bandahm")
        cursor = connection.cursor()
        for sql in listaSql:
            cursor.execute(sql)
        connection.commit()
    except:
        print("Error guardar sql")
    finally:
        if connection:
            cursor.close()
            connection.close()

def obtenerInformacionFecha(cadena):
    nombre = cadena.split("_")[-1]
    anio =  nombre[0:2]
    mes = nombre[2:4]
    dia = nombre[4:6]
    hora = nombre[6:8]
    minuto = nombre[8:10]
    segundo = nombre[10:12]

    print(f" año {anio} , mes {mes}, día {dia}, Hora {hora}:{minuto}:{segundo}")
def obtenerUltimoRegistro():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="admin",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="bandahm")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM test.m5090_d1_4211m ORDER by id DESC LIMIT 1;")
        registro = cursor.fetchall()
        print(registro)
        connection.commit()
    except:
        print("Error guardar sql")
    finally:
        if connection:
            cursor.close()
            connection.close()


