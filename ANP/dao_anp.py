from model import *
SQL_BUSCA = 'SELECT * FROM correntes_anp ORDER BY Corrente ASC'
SQL_DELETA = 'DELETE FROM correntes_anp WHERE Ide = %s'
SQL_CRIA = 'INSERT INTO correntes_anp (Corrente, Tipo, Bacia, API, Nafta, Medios, Resíduo) VALUES (%s, %s, %s, %s, %s, %s, %s)'
SQL_ATUALIZAR = 'UPDATE correntes_anp SET Corrente = %s, Tipo=%s, Bacia=%s, API=%s, Nafta=%s, Medios=%s, Resíduo=%s WHERE ide=%s'
SQL_POR_ID = 'SELECT ide, Corrente, Tipo, Bacia, API, Nafta, Medios, Resíduo FROM correntes_anp WHERE ide = %s'
SQL_COUNT_TIPO = 'SELECT COUNT(Tipo) AS Tipos FROM correntes_anp GROUP BY Tipo'
SQL_COUNT = 'SELECT COUNT(Tipo) AS Tipos FROM correntes_anp'
SQL_Pesado = 'SELECT MIN(API) As Pesado FROM correntes_anp'
SQL_Leve = 'SELECT MAX(API) As Leve FROM correntes_anp'
SQL_Quant_PC = 'SELECT Tipo, COUNT(Tipo) AS Quantidade FROM correntes_anp GROUP BY Tipo'
SQL_BACIA = 'SELECT Bacia, COUNT(Bacia) AS Quantidade FROM correntes_anp GROUP BY Bacia ORDER BY Quantidade DESC'
SQL_CARAC = 'SELECT Tipo, AVG(Nafta) AS Nafta_media, AVG(Medios) AS Diesel_media, AVG(Resíduo) AS Residuo_media FROM correntes_anp GROUP BY Tipo'
SQL_CARAC_BACIA = 'SELECT Bacia, AVG(Nafta) AS Nafta_media, AVG(Medios) AS Diesel_media, AVG(Resíduo) AS Residuo_media FROM correntes_anp GROUP BY Bacia'

class DAO:
    def __init__(self, db):
        self.__db = db

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA)
        atividade = traduz_atividade(cursor.fetchall())
        return atividade

    def apagar(self,ide):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_DELETA, (ide,))
        self.__db.connection.commit()

    def busca_por_id(self, ide):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_POR_ID, (ide,))
        tupla = cursor.fetchone()
        return ANP(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], ide=tupla[0])

    def salvar(self,lista):
        cursor = self.__db.connection.cursor() #cursor para acessar o db
        if lista.ide:
            cursor.execute(SQL_ATUALIZAR,(lista.corrente, lista.tipo, lista.bacia, lista.api, lista.nafta, lista.medio, lista.residuo, lista.ide))
        else:
            cursor.execute(SQL_CRIA, (lista.corrente, lista.tipo, lista.bacia, lista.api, lista.nafta, lista.medio, lista.residuo))
        self.__db.connection.commit()
        return lista

    def contagem(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_COUNT)
        count_cor = cursor.fetchall()
        return count_cor

    def max_api(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_Leve)
        leve = cursor.fetchall()
        return leve

    def min_api(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_Pesado)
        pesado = cursor.fetchall()
        return pesado

    def qtd_pet(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_Quant_PC)
        quant = cursor.fetchall()
        return quant

    def qtd_bacia(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BACIA)
        bacia = cursor.fetchall()
        return bacia

    def caract_tipo(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CARAC)
        carac = cursor.fetchall()
        return carac

    def caract_bacia(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CARAC_BACIA)
        carac = cursor.fetchall()
        return carac

def traduz_atividade(atividades):
    def cria_atividade_com_tupla(tupla):
        return ANP(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], ide=tupla[0])
        
    return list(map(cria_atividade_com_tupla, atividades))   
