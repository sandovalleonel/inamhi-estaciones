
#consultarDatos("select * from Administrativo.provincias")
from guardar_datos.ConnPostgres import ingresarPostgresUno

ingresarPostgresUno("INSERT INTO administrativo.accesos( id_acceso, nombre, descripcion) VALUES (989,'leo','admin');")