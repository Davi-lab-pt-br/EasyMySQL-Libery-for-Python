import mysql.connector

class Connect():
    @staticmethod
    def connection():
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin',
            database='bdyoutube'
        )
    
    def connection_close():
        mysql.connector.connect(
            host='Your host',
            user='Your user',
            password='Your password',
            database='Your database'
        ).close()

class CURSOR:
    def __init__(self):
        self.conexao = Conectar.conexao()  # Usando a conexão da classe Conectar
        self.cursor = self.conexao.cursor()

    def executar_comando(self,comando):
        self.cursor.execute(comando)

    def fechall(self):
        self.cursor.fetchall()

    def close(self):
        self.cursor.close()
