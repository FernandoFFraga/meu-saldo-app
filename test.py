from app.controller.lancamento_despesa_controller import select_by_id
from dotenv import load_dotenv

# Carrega variaveis de ambiente
load_dotenv()

if __name__ == '__main__':
    item = select_by_id(11)
    print(item.descricao)
