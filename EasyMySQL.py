import mysql.connector

class Connect():
    @staticmethod
    def connetion():
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin',
            database='bdyoutube'
        )

class CURSOR:
    def __init__(self):
        self.connection = Connect.connection()  
        self.cursor = self.connection.cursor()

    def executar_comando(self,command):
        self.cursor.execute(command)
