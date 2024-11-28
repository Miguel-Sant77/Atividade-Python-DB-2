import mysql.connector

def create_database_and_table():
    # Conexão ao MySQL
    conn = mysql.connector.connect(
        host='localhost',
        user='seu_usuario',  # substitua pelo seu usuário
        password='sua_senha'  # substitua pela sua senha
    )
    cursor = conn.cursor()

    # Criação da base de dados
    cursor.execute("CREATE DATABASE IF NOT EXISTS minha_base_de_dados")
    cursor.execute("USE minha_base_de_dados")

    # Criação da tabela
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS minha_tabela (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            idade INT,
            salario DECIMAL(10, 2),
            data_admissao DATE
        )
    """)

    # Fechando a conexão
    conn.commit()
    cursor.close()
    conn.close()

create_database_and_table()
