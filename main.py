from tinydb import TinyDB, Query
import pandas as pd
from rich import print

# TinyDB set
db = TinyDB("./storage/data.json")
dataQuery = Query()

# TODO> função para cadastrar veiculos no banco de dados
def cadastrar_veiculo():
    """
    * Input de inteiro do número frota do carro, e valida se já existe
    no BD.
    * Se NÃO existir ele vai pedir também a placa e cadastrar no mesmo.
    * Se EXISTIR ele vai retornar uma mensagem informando a existência.
    """
    frota = str(input("Frota: ")).upper()
    validation = db.search(dataQuery.Frota == frota)
    if validation == []:
        placa = str(input("Placa: ")).upper()
        db.insert(
            {
                "Frota": frota,
                "Placa": placa,
                "Despesas": [],
            }
        )
    else:
        print("\n* [white on dark_orange3 b]Veículo já está no cadastro![/]\n")


# TODO> função para adicionar produto ou serviço ao veiculo
def adicionar_despesa():
    # Input de Frota, NF e Valor.
    while True:
        frota = str(input("Frota: ")).upper()
        # a variavel (item) recebe o "dict" todo onde contém a "chave" de nome (Frota) // (db.search) adiciona o dict a um list, ficando assim. [{}]
        item = db.search(dataQuery.Frota == frota)
        if len(item) == 0:
            print("\n* [white on dark_orange3 b]Veículo não cadastrado![/]\n")
        else:
            break

    # input do numero da NOTA e do VALOR.
    nf = str(input("NF: "))
    valor = float(input("R$: "))
    desc = str(input("Descrição: "))
    # Cria um dicionário com numero da NOTA FISCAL e o VALOR inserido no input.
    despesa = {"NF": nf, "R$": valor, "Descricao": desc}

    # acessando o primeiro item [0] (dict) contido na lista e buscando todas "chaves" de nome "Despesas".
    item[0]["Despesas"].append(despesa)
    db.update(item[0], doc_ids=[item[0].doc_id])


# TODO> função para procurar veiculos no banco de dados
def procurar_veiculo():
    # input de veiculo frota.
    frota = str(input("Frota: ")).upper()
    # busca o valor passado no input e se encontrado coleta o dict com todos dados dentro de uma list. [{}]
    bloco = db.search(dataQuery.Frota == frota)
    n_nf = []
    v_nf = []
    desc_nf = []

    # valida se o "db.search" encontrou o número do veículo "frota" informado.
    if bloco == []:
        print("\n* [white on green1 b]Veículo não encontrado![/]\n")
    else:
        for dict_nf in bloco:
            # Pegando a placa do veiculo somente para usar no nome do arquivo xlsx
            placa = dict_nf["Placa"]
            for despesas in dict_nf["Despesas"]:
                # Pegando todos os dados contidos dentro de despesas, encapsulando em uma lista para passar ao pandas.
                n_nf.append(despesas["NF"])
                v_nf.append(despesas["R$"])
                desc_nf.append(despesas["Descricao"])
        # Criando o dict para passar ao Pandas
        table = {"NF": n_nf, "R$": v_nf, "Descrição": desc_nf}
        df = pd.DataFrame(table)
        # Criando tabela do excel com dataframe.
        df.to_excel(f"{placa}.xlsx")
        # Imprimindo os valores do dataframe.
        print(f"\n➜ [white on dark_orange3 b]{placa}[/]")
        print(f"\n{df}")
        total = df["R$"].sum()
        print(f"[white on dark_orange3 b]Total: R${total:.2f}[/]")


# TODO> menu de opções
while True:
    print(
        """\n
    [white on blue_violet b](1): Cadastrar Veículos[/] 
    [white on blue_violet b](2): Procurar Veículos[/]  
    [white on blue_violet b](3): Adicionar Despesas[/] 
    [white on blue_violet b](5): Sair[/]               
    \n"""
    )
    condition = int(input("► "))
    if condition == 1:
        cadastrar_veiculo()
    elif condition == 2:
        procurar_veiculo()
    elif condition == 3:
        adicionar_despesa()
    else:
        break
