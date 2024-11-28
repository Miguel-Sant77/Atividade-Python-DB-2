def insert_data():
    conn = mysql.connector.connect(
        host='localhost',
        user='seu_usuario',
        password='sua_senha',
        database='minha_base_de_dados'
    )
    cursor = conn.cursor()

    # Inserir um registro
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    idade = input("Digite a idade: ")
    salario = input("Digite o salário: ")
    data_admissao = input("Digite a data de admissão (YYYY-MM-DD): ")

    cursor.execute("""
        INSERT INTO minha_tabela (nome, email, idade, salario, data_admissao) 
        VALUES (%s, %s, %s, %s, %s)
    """, (nome, email, idade, salario, data_admissao))

    # Inserir dois registros de uma vez
    registros = []
    for _ in range(2):
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        idade = input("Digite a idade: ")
        salario = input("Digite o salário: ")
        data_admissao = input("Digite a data de admissão (YYYY-MM-DD): ")
        registros.append((nome, email, idade, salario, data_admissao))

    cursor.executemany("""
        INSERT INTO minha_tabela (nome, email, idade, salario, data_admissao) 
        VALUES (%s, %s, %s, %s, %s)
    """, registros)

    conn.commit()
    cursor.close()
    conn.close()

insert_data()
