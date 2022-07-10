import psycopg2

user="postgres"
password="postgres"
host="127.0.0.1"
port="5432"
database="inamhi"


def guardar(lista,nombreEstacion,nombreFichero):

    codigoFecha = obtenerInformacionFecha(nombreFichero)

    nombreEstacion = nombreEstacion.split(".")[0]
    lista_Guardar = []
    sqlTabla = ""
    opc=[[0]]
    for val in lista:
        nombreTabla = nombreEstacion+"_"+val[0].split('_')[1]
        print(nombreTabla)
        #opc = InsertOrUpdate(nombreTabla,codigoFecha[0])
   

        if(opc[0][0] == 0):
            sqlTabla = (f"insert into test.{nombreTabla} ( fecha_creacion, fecha_archivo, nom, resultado_{codigoFecha[1]},tot_proce_{codigoFecha[1]})values('1996-12-02','{codigoFecha[0]}','none','{val[1]}','{val[2]}');")
        if(opc[0][0] != 0):
            sqlTabla = (f"update  test.{nombreTabla} set resultado_{codigoFecha[1]}='{val[1]}',tot_proce_{codigoFecha[1]}='{val[2]}';")
        lista_Guardar.append(sqlTabla)
    crearConexionYGuardar(lista_Guardar)
    ###########guardar




def crearConexionYGuardar(listaSql):
   
    try:
        connection = psycopg2.connect(user=user,password=password, host=host,port=port,database=database)
        cursor = connection.cursor()
        for sql in listaSql:
            #print(sql)
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
    #print(f" año {anio} , mes {mes}, día {dia}, Hora {hora}:{minuto}:{segundo}")
    return [anio+mes+dia+hora,minuto]


def InsertOrUpdate(nombreTabla,codigoFecha):
    registro = 0
    try:
        connection = psycopg2.connect(user=user,password=password, host=host,port=port,database=database)
        cursor = connection.cursor()
        cursor.execute(f"SELECT count(*) FROM test.{nombreTabla}  where fecha_archivo='{codigoFecha}';")
        registro = cursor.fetchall()
        connection.commit()
    except:
        print("Error consultar sql")
    finally:
        if connection:
            cursor.close()
            connection.close()
    
    return registro


