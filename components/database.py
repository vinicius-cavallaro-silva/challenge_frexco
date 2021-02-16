import sqlite3


class Database:

    def connection(self):
        #criando a conexão
        self.conn = sqlite3.connect('automacoes.db')
        print("Criando a conexão com o banco de dados.")
        return self.conn

    def create_table(self):
        cursor = self.conn.cursor()
        query_sql = '''CREATE TABLE FRUBANA
                         (
                         PRODUCT        TEXT    NOT NULL,
                         PRECO          TEXT,
                         UNIDADE        TEXT,
                         OBSERVACOES    TEXT);
                         '''
        cursor.execute(query_sql)
        print("Tabela criada com sucesso!")

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

        print("Dados inseridos com sucesso!")


    def close_connection(self):
        self.conn.close()