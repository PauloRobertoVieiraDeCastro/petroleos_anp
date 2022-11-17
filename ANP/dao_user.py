from model import *
SQL_USUARIO = 'SELECT Nome, Senha FROM Logando WHERE Nome = %s'

class DAO_USER:
    def __init__(self, db):
        self.__db = db

    def usuario(self,nome):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO,(nome,))
        a = cursor.fetchall()
        return a
