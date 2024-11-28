def query_data():
    conn = mysql.connector.connect(
        host='localhost',
        user='seu_usuario',
        password='sua_senha',
        database='minha_base_de_dados'
    )
    cursor = conn.cursor()

    valor_pesquisa = input("Digite o valor para pesquisa no email: ")
    cursor.execute("SELECT * FROM minha_tabela WHERE email LIKE %s", ('%' + valor_pesquisa + '%',))
    
    results = cursor.fetchall()

    if not results:
        print("Tabela vazia.")
    else:
        print("Resultados na horizontal:")
        for row in results:
            print(row)

        print("\nResultados na vertical:")
        for row in results:
            for item in row:
                print(item)
            print("-----")  # Separador entre registros

    cursor.close()
    conn.close()

query_data()
