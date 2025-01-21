class CategoriaRendimento:

    def __init__(self, nome=None, id=None, data_criacao=None):
        self.id = id
        self.nome = nome
        self.data_criacao = data_criacao

    def set(self, rs):
        if rs is None:
            return

        self.id = rs.get('id', None)
        self.nome = rs.get('nome', None)

        return self