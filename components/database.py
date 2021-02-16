import sqlite3
from components.utils import logger


class Database:

    def connection(self):
        #criando a conexão
        self.conn = sqlite3.connect('automacoes.db')
        logger("Criando a conexão com o banco de dados...")
        return self.conn

    def drop_table(self):

        self.cursor = self.conn.cursor()
        query_sql_drop_table = '''drop table if exists FRUBANA'''
        self.cursor.execute(query_sql_drop_table)
        logger("Tabela deletada com sucesso, para a criação de uma nova.")

    def create_table(self):
        self.drop_table()
        query_sql = '''create table if not exists FRUBANA
                         (
                         PRODUCT        TEXT    NOT NULL,
                         PRECO          TEXT,
                         UNIDADE        TEXT,
                         OBSERVACOES    TEXT);
                         '''
        self.cursor.execute(query_sql)
        logger("Tabela criada com sucesso!")

    def insert_data(self, list_data):

        for item in list_data:
            product = item[0]
            preco = item[1]
            unidade = item[2]

            if len(item) >= 4:
                observacao = item[3]
                self.conn.execute("""INSERT INTO FRUBANA (PRODUCT, PRECO, UNIDADE, OBSERVACOES) \
                                          VALUES (?, ?, ?, ?);""", (product, preco, unidade, observacao))

                self.conn.commit()
            else:
                observacao = "nenhuma"
                self.conn.execute("""INSERT INTO FRUBANA (PRODUCT, PRECO, UNIDADE, OBSERVACOES) \
                                          VALUES (?, ?, ?, ?);""", (product, preco, unidade, observacao))

                self.conn.commit()

        logger("Dados inseridos com sucesso!")


    def close_connection(self):
        self.conn.close()