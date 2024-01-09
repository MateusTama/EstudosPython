def criarTabelas(parCursor):
    # Tabela veículos:
    # - Campos: id AUTO INCREMENT, marca, modelo, ano, 
    # cor, placa, PK (id).
    sql = """CREATE TABLE IF NOT EXISTS 
                        veiculos (
                            id INT NOT NULL AUTO_INCREMENT,
                            marca VARCHAR(50),
                            modelo VARCHAR(50),
                            ano INT,
                            cor VARCHAR(50),
                            placa CHAR(7),
                            PRIMARY KEY (id)
                        )"""
    try:
        parCursor.execute(sql)
        print("Tabela veiculos criada com sucesso.")
    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")

    # Tabela cruzamentos:
    # - Campos: id AUTO INCREMENT, rua1, rua2, PK (id)
    sql = """CREATE TABLE IF NOT EXISTS 
                        cruzamentos (
                           id INT NOT NULL AUTO_INCREMENT,
                           rua1 VARCHAR(50),
                           rua2 VARCHAR(50),
                           PRIMARY KEY (id) 
                        )"""
    try:
        parCursor.execute(sql)
        print("Tabela cruzamentos criada com sucesso.")
    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")

    # Tabela leituras:
    # - Campos: id AUTO INCREMENT, id cruzamento, placa, 
    # PK (id), FK (id cruzamento)
    sql = """CREATE TABLE IF NOT EXISTS
                        leituras (
                            id INT NOT NULL AUTO_INCREMENT,
                            id_cruzamento INT NOT NULL,
                            placa CHAR(7),
                            PRIMARY KEY (id),
                            FOREIGN KEY (id_cruzamento) 
                                REFERENCES cruzamentos(id)
                        )"""
    try:
        parCursor.execute(sql)
        print("Tabela leituras criada com sucesso.")
    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")

def inserirCarros(parCursor):
    # - Insira 10 carros (a seu critério).
    sql = []
    # carro 1
    sql.append( """INSERT INTO 
                            veiculos
                                (marca, modelo, ano, cor, placa)
                            VALUES
                                ('citroen','c3',2018,'prata','QRJ5877')
                """)
    # carro 2
    sql.append( """INSERT INTO 
                            veiculos
                                (marca, modelo, ano, cor, placa)
                            VALUES
                                ('honda','city',2020,'branco','KTR5394')
                """)
    # carro 3
    sql.append( """INSERT INTO 
                            veiculos
                                (marca, modelo, ano, cor, placa)
                            VALUES
                                ('fiat','argo',2019,'vermelho','LHS3989')
                """)    
    # carro 4
    sql.append( """INSERT INTO 
                            veiculos
                                (marca, modelo, ano, cor, placa)
                            VALUES
                                ('vw','up',2019,'preto','OMF1464')
                """)  
    # carro 5
    sql.append( """INSERT INTO 
                            veiculos
                                (marca, modelo, ano, cor, placa)
                            VALUES
                                ('gm','cruze',2021,'cinza','HQA6780')
                """)               
    # carro 6
    sql.append( """INSERT INTO 
                            veiculos
                                (marca, modelo, ano, cor, placa)
                            VALUES
                                ('peugeot','307',2020,'branco','LDW4698')
                """)                
    # carro 7
    sql.append( """INSERT INTO 
                            veiculos
                                (marca, modelo, ano, cor, placa)
                            VALUES
                                ('jeep','renegade',2019,'marrom','PGF5888')
                """)                
    # carro 8
    sql.append( """INSERT INTO 
                            veiculos
                                (marca, modelo, ano, cor, placa)
                            VALUES
                                ('ford','focus',2015,'azul','HMB5456')
                """)                               
    # carro 9
    sql.append( """INSERT INTO 
                            veiculos
                                (marca, modelo, ano, cor, placa)
                            VALUES
                                ('vw','virtus',2021,'prata','DJL1624')
                """)                               
    # carro 10
    sql.append( """INSERT INTO 
                            veiculos
                                (marca, modelo, ano, cor, placa)
                            VALUES
                                ('renault','kwid',2020,'branco','JGB9337')
                """)

    try:
        for comando in sql:
            parCursor.execute(comando)
        print("Carros inseridos com sucesso.")
    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")    

def inserirCruzamentos(parCursor):
    # - Insira 5 cruzamentos (a seu critério).
    sql = []
    # cruzamento 1
    sql.append( """INSERT INTO 
                            cruzamentos
                                (rua1, rua2)
                            VALUES
                                ('hercilio luz','manoel tavares')
                """)
    # cruzamento 2
    sql.append( """INSERT INTO 
                            cruzamentos
                                (rua1, rua2)
                            VALUES
                                ('rodrigues alves','adriano schaeffer')
                """)  
    # cruzamento 3
    sql.append( """INSERT INTO 
                            cruzamentos
                                (rua1, rua2)
                            VALUES
                                ('otto renaux','barao do rio branco')
                """)                
    # cruzamento 4
    sql.append( """INSERT INTO 
                            cruzamentos
                                (rua1, rua2)
                            VALUES
                                ('paes leme','riachuelo')
                """) 
    # cruzamento 5
    sql.append( """INSERT INTO 
                            cruzamentos
                                (rua1, rua2)
                            VALUES
                                ('humberto mattiolli','carlos appel')
                """)                               
    try:
        for comando in sql:
            parCursor.execute(comando)
        print("Cruzamentos inseridos com sucesso.")
    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")                 

def inserirLeituras(parCursor, parLeituras):

    for leitura in range(parLeituras):
        idCruzamento = input("Id cruzamento: ")
        placaLida = input("Placa lida: ")
        sql = f"""INSERT INTO leituras (id_cruzamento, placa)
                        VALUES ({idCruzamento} , '{placaLida}')"""
        try:
            parCursor.execute(sql)
        except Exception as erro:
            print(f"Ocorreu um erro: {erro}")

    print("Fim do processamento das leituras. Verifique o banco de dados.")