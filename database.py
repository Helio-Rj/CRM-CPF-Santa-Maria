import sqlite3


class Data_base:

    def __init__(self, name='clientes.db') -> None:
        self.name = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    def create_table_cliente(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Clientes(

            CPF TEXT,
            NOME TEXT,
            RG TEXT,
            ORGAO_EXPEDITOR TEXT,
            DATA_EXPEDICAO TEXT,
            DATA_NASCIMENTO TEXT,
            NOME_MAE TEXT,            
            LOGRADOURO TEXT,
            NUMERO TEXT,
            COMPLEMENTO TEXT,
            BAIRRO TEXT,
            MUNICIPIO TEXT,
            UF TEXT,
            CEP TEXT,
            TELEFONE TEXT,
            EMAIL TEXT,
            ACEITE TEXT,
            DATA_INSTALACAO TEXT,

            PRIMARY KEY(CPF)
            );




        """)

    def register_cliente(self, fullDataSet):

        campos_tabela = ('CPF', 'NOME', 'RG', 'ORGAO_EXPEDITOR', 'DATA_EXPEDICAO', 'DATA_NASCIMENTO', 'NOME_MAE',
                         'LOGRADOURO', 'NUMERO', 'COMPLEMENTO', 'BAIRRO', 'MUNICIPIO', 'UF', 'CEP', 'TELEFONE',
                         'EMAIL' 'ACEITE', 'DATA_INSTALACAO')

        qntd = "?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?"
        cursor = self.connection.cursor()

        try:
            cursor.execute(f"""INSERT INTO Clientes {campos_tabela}
            VALUES({qntd})""", fullDataSet)
            self.connection.commit()
            return "OK"

        except:
            return "Error"

    def select_all_clientes(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Empresas ORDER BY NOME")
            empresas = cursor.fetchall()
            return empresas
        except:
            pass

    def delete_cliente(self, id):

        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Clientes WHERE CPF = '{id}' ")

            self.connection.commit()

            return "Cadastro de cliente excluido com sucesso!"

        except:
            return "Erro ao Excluir registro!"

    def update_cliente(self, fullDataSet):

        cursor = self.connection.cursor()
        cursor.execute(f""" UPDATE Clientes set

            CPF = '{fullDataSet[0]}',
            NOME = '{fullDataSet[1]}',
            RG = '{fullDataSet[2]}',
            ORGAO_EXPEDITOR = '{fullDataSet[3]}',
            DATA_EXPEDICAO = '{fullDataSet[4]}',
            DATA_NASCIMENTO = '{fullDataSet[5]}',
            NOME_MAE = '{fullDataSet[6]}',
            LOGRADOURO = '{fullDataSet[7]}',
            NUMERO = '{fullDataSet[8]}',
            COMPLEMENTO = '{fullDataSet[9]}',
            BAIRRO = '{fullDataSet[10]}',
            MUNICIPIO = '{fullDataSet[11]}',
            UF = '{fullDataSet[12]}',
            CEP = '{fullDataSet[13]}',
            TELEFONE = '{fullDataSet[14]}',
            EMAIL = '{fullDataSet[15]}'
            ACEITE = '{fullDataSet[16]}'
            DATA_INSTALACAO = '{fullDataSet[17]}'
            

            WHERE CPF = '{fullDataSet[0]}'""")

        self.connection.commit()
