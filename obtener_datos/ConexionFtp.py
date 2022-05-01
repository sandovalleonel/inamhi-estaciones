from  ftplib import  FTP

class ConexionFtp:


    def __init__(self, host, usuario, contrasenia, listar_Urls , destino):
        self.host = host
        self.usuario = usuario
        self.contrasenia = contrasenia
        self.listar_Urls = listar_Urls
        self.destino = destino

    def connn(self):
        print("*************")
        ftp = FTP(self.host)  # connect to host, default port
        ftp.login(self.usuario,self.contrasenia)  # user anonymous, passwd anonymous@
        ftp.encoding = "utf-8"
        ftp.cwd(self.listar_Urls)
        #ftp.retrlines('LIST')
        ftp.nlst()
        #print(ftp.pwd())
        print("*************")