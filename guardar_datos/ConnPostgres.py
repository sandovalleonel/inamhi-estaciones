import psycopg2
from guardar_datos.bd import conexion

def ingresarPostgresMuchos(listaSQL):

    try:
        with conexion.cursor() as cursor:
            for sql in listaSQL:
                cursor.execute(sql)
        conexion.commit()

    except psycopg2.Error as e:
        print("Ocurrió un error al insertar: ", e)
    finally:
        conexion.close()


def ingresarPostgresUno(SQL):
    try:
        with conexion.cursor() as cursor:
            cursor.execute(SQL)
        conexion.commit()

    except psycopg2.Error as e:
        print("Ocurrió un error al insertar: ", e)
    finally:
        conexion.close()


def consultarDatos(SQL):
    try:
        with conexion.cursor() as cursor:

            cursor.execute(SQL)
            datosEstacion = cursor.fetchall()

            # Recorrer e imprimir
            for estacion in datosEstacion:
                print(estacion)
    except psycopg2.Error as e:
        print("Ocurrió un error al consultar: ", e)
    finally:
        conexion.close()

#ingresarPostgresUno("INSERT INTO administrativo.accesos( id_acceso, nombre, descripcion) VALUES (989,'leo','admin');")
#consultarDatos("select * from Administrativo.provincias")