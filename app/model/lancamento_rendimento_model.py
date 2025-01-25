class LancamentoRendimento:
    def __init__(self,
                 id=None,
                 id_categoria=None,
                 descricao=None,
                 valor=None,
                 uuid_sequencia=None,
                 data_efetiva=None,
                 data_inclusao=None):

        self.id = id
        self.id_categoria = id_categoria
        self.descricao = descricao
        self.valor = valor
        self.uuid_sequencia = uuid_sequencia
        self.data_efetiva = data_efetiva
        self.data_inclusao = data_inclusao

    def set(self, rs):

        if rs is None:
            return

        self.id = rs.get('id', None)
        self.id_categoria = rs.get('id_categoria', None)
        self.descricao = rs.get('descricao', None)
        self.valor = rs.get('valor', None)
        self.uuid_sequencia = rs.get('uuid_sequencia', None)
        self.data_efetiva = rs.get('data_efetiva', None)

        return self