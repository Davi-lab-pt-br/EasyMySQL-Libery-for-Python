import mysql.connector

class Connect():
    @staticmethod
    def Connection():
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

    def connection_close_other_alternative():
        Connect.Connection.close()

class CURSOR:
    def __init__(self):
        self.connection = Connect.Connection()  # Usando a conexão da classe Conectar
        self.cursor = self.Conexao.cursor()

    def executar_comando(self,command):
        self.cursor.execute(command)

    def fechall(self):
        self.cursor.fetchall()

    def close(self):
        self.cursor.close()
