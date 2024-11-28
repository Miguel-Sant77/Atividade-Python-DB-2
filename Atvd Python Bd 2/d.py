def delete_data():
    conn = mysql.connector.connect(
        host='localhost',
        user='seu_usuario',
        password='sua_senha',
        database='minha_base_de_dados'
    )
    cursor = conn.cursor()

    valor_email = input("Digite o email do registro que deseja apagar: ")
    cursor.execute("DELETE FROM minha_tabela WHERE email = %s", (valor_email,))

    if cursor.rowcount == 0:
        print("Nenhum registro encontrado para o email fornecido.")
    else:
        print("Registro apagado com sucesso.")

    conn.commit()
    cursor.close()
    conn.close()

delete_data()
