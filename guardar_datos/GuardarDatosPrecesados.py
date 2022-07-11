import psycopg2

user="postgres"
password="postgres"
host="127.0.0.1"
port="5432"
database="inamhi"


def guardar(lista,nombreEstacion,nombreFichero):
    codigoFecha = obtenerInformacionFecha(nombreFichero)
    nombreEstacion = nombreEstacion.split(".")[0]
    crearConexionYGuardar(lista,nombreEstacion,codigoFecha)




def crearConexionYGuardar(ArrayDatos,estacionNombre,codigoFecha):
    sql_insert = ""
    sql_select = ""
    try:
        connection = psycopg2.connect(user=user,password=password, host=host,port=port,database=database)
        cursor = connection.cursor()
        for val in ArrayDatos:
            nombreTabla = estacionNombre+"_"+val[0].split('_')[1]
            cursor.execute(f"SELECT count(*) FROM test.{nombreTabla}  where fecha_archivo='{codigoFecha[0]}';")
            sql_select=(f"SELECT count(*) FROM test.{nombreTabla}  where fecha_archivo='{codigoFecha[0]}';")
            existenRegistros = cursor.fetchall()
            if(existenRegistros[0][0] == 0):
                cursor.execute (f"insert into test.{nombreTabla} ( fecha_creacion, fecha_archivo, nom, resultado_{codigoFecha[1]},tot_proce_{codigoFecha[1]})values('1996-12-02','{codigoFecha[0]}','none','{val[1]}','{val[2]}');")
                sql_insert=(f"insert into test.{nombreTabla} ( fecha_creacion, fecha_archivo, nom, resultado_{codigoFecha[1]},tot_proce_{codigoFecha[1]})values('1996-12-02','{codigoFecha[0]}','none','{val[1]}','{val[2]}');")
            if(existenRegistros[0][0] != 0):
                cursor.execute (f"update  test.{nombreTabla} set resultado_{codigoFecha[1]}='{val[1]}',tot_proce_{codigoFecha[1]}='{val[2]}';")
                sql_insert = (f"update  test.{nombreTabla} set resultado_{codigoFecha[1]}='{val[1]}',tot_proce_{codigoFecha[1]}='{val[2]}';")

        connection.commit()
    except:
        print("Error guardar sql")
        print(sql_select)
        print(sql_insert)
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



