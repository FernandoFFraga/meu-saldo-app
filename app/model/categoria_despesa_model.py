class CategoriaDespesa:
    def __init__(self, nome=None, limite_mensal=None, id=None, data_criacao=None):
        self.id = id
        self.nome = nome
        self.limite_mensal = limite_mensal
        self.data_criacao = data_criacao

    def set(self, rs):

        if rs is None:
            return

        self.id = rs.get('id', None)
        self.nome = rs.get('nome', None)
        self.limite_mensal = rs.get('limite_mensal', None)

        return self

