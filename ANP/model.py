
class ANP:
    def __init__(self,corrente,tipo,bacia,api,nafta,medio,residuo,ide=None):
        self.corrente = corrente
        self.tipo = tipo
        self.bacia = bacia
        self.api = api
        self.nafta = nafta
        self.medio = medio
        self.residuo = residuo
        self.ide = ide

class Usuario:
    def __init__(self,nome,senha):
        self.nome = nome
        self.senha = senha
