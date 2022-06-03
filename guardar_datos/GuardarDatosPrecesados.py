

def guardar(lista):
    lista_Guardar = []
    for val in lista:
        creartablas = (f"""
            CREATE TABLE IF NOT EXISTS test.M{val[0]}(
               id SERIAL PRIMARY KEY,
               nom VARCHAR NOT NULL,
               res VARCHAR NOT NULL,
               tot VARCHAR NOT NULL
            );
        """)

        insertarTablas = (f"insert into test.M{val[0]} (nom,res,tot)values('nada','{val[1]}','{val[2]}');")
        lista_Guardar.append(insertarTablas)
    print(lista_Guardar)
    return  lista_Guardar
