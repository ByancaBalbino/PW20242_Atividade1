SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS produto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT  NOT NULL,
        descrição TEXT NOT NULL,
        preço FLOAT,
        data_nascimento DATE NOT NULL,
        estoque INTEGER

    )
"""