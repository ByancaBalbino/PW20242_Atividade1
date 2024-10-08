from models.produto_model import *
from sql.produto_sql import*
from util import obter_conexao
from typing import List, Optional




def criar_tabela():
    with obter_conexao() as conexao:
        db = conexao.cursor()
        db.execute(SQL_CRIAR_TABELA)


def inserir(prdouto: Produto) -> Optional[Produto]:
    with obter_conexao() as conexao:
        db = conexao.cursor()
        db.execute(SQL_INSERIR,
           (Produto.nome,
            Produto.descricao,
            Produto.estoque,
            Produto.id,
            Produto.preco,
            Produto.categoria,))
        if db.rowcount > 0:
            Produto.id = db.lastrowid
            return Produto
        else:
            return None

def obter_todos() -> List[Produto]:
    with obter_conexao() as conexao:
        db = conexao.cursor()
        tuplas = db.execute(SQL_OBTER_TODOS).fetchall()
        usuarios = [Produto(*t) for t in tuplas]
        return usuarios
