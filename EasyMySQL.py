import mysql.connector

class Connect():
    @staticmethod
    def connetion():
        return mysql.connector.connect(
            host='your host',
            user='your user',
            password='your password',
            database='your database'
        )

class CURSOR:
    def __init__(self):
        self.connection = Connect.connection()  
        self.cursor = self.connection.cursor()

    def executar_comando(self,command):
        self.cursor.execute(command)
