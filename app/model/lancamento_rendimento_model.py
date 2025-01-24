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