# Grupo:
# Adolfo Kentaro Hada   RM:556884
# Bruno Otavio SIlva de Oliveira   RM:556196
# Guilherme Flores Pereira de Almeida   RM:554948
# Luiz Fernando de Aragão Souza   RM:555561
# Marcello de Freitas Almeida   RM:557531



# Lista principal que armazena os insumos como dicionários
#Estoque = []

# Estoque para meus testes
Estoque = [
    {
        "id": 101,
        "nome": "Soro Fisiológico 0.9%",
        "local": "Enfermaria",
        "quantidade": 12,
        "ideal": 20
    },
    {
        "id": 102,
        "nome": "Luvas Cirúrgicas",
        "local": "Centro Cirúrgico",
        "quantidade": 5,
        "ideal": 30
    },
    {
        "id": 103,
        "nome": "Máscaras N95",
        "local": "UTI",
        "quantidade": 50,
        "ideal": 50
    },
    {
        "id": 104,
        "nome": "Seringas 5ml",
        "local": "Farmácia",
        "quantidade": 25,
        "ideal": 40
    },
    {
        "id": 105,
        "nome": "Álcool Gel",
        "local": "Recepção",
        "quantidade": 8,
        "ideal": 15
    },
    {
        "id": 106,
        "nome": "Paracetamol 500mg",
        "local": "Farmácia",
        "quantidade": 100,
        "ideal": 90
    }
]




# Função para inserir um novo insumo no estoque
# Complexidade: O(1) para inserção em lista
# Inputs são coletados via terminal; verifica tipo dos dados
# Adiciona um dicionário de insumo à lista Estoque
def InserirInsumo():
    try:
        id = int(input("ID do insumo: "))
        nome = input("Nome do insumo: ")
        local = input("Local (Enfermaria, UTI, Farmácia, etc): ")
        quantidade = int(input("Quantidade atual: "))
        ideal = int(input("Quantidade ideal: "))

        insumo = {
            "id": id,
            "nome": nome,
            "local": local,
            "quantidade": quantidade,
            "ideal": ideal
        }

        Estoque.append(insumo)
        print("Insumo adicionado com sucesso!")

    except ValueError:
        print("Erro: ID, Quantidade e Ideal devem ser números inteiros.")

# Função para identificar o insumo mais urgente em falta
# Um insumo está em falta se sua quantidade < ideal
# Complexidade: O(n^2) pela ordenação manual com dois loops aninhados
def ProximoInsumoEmFalta():
    em_falta = []

    # Filtra insumos com quantidade abaixo do ideal
    for insumo in Estoque:
        if insumo["quantidade"] < insumo["ideal"]:
            em_falta.append(insumo)

    if not em_falta:
        print("Nenhum insumo em falta no momento.")
        return

    # Ordenação manual por maior diferença entre ideal e atual
    for i in range(len(em_falta)):
        for j in range(i + 1, len(em_falta)):
            falta_i = em_falta[i]["ideal"] - em_falta[i]["quantidade"]
            falta_j = em_falta[j]["ideal"] - em_falta[j]["quantidade"]
            if falta_j > falta_i:
                em_falta[i], em_falta[j] = em_falta[j], em_falta[i]

    # Exibe o insumo com maior urgência
    mais_urgente = em_falta[0]
    print("\n--- Insumo Mais Urgente ---")
    print("ID:", mais_urgente["id"])
    print("Nome:", mais_urgente["nome"])
    print("Local:", mais_urgente["local"])
    print("Quantidade Atual:", mais_urgente["quantidade"])
    print("Quantidade Ideal:", mais_urgente["ideal"])

# Atualiza a quantidade de um insumo com base no ID informado
# Complexidade: O(n) - busca linear pelo ID
def AtualizarQuantidade():
    try:
        id_insumo = int(input("Digite o ID do insumo a ser atualizado: "))
        nova_quantidade = int(input("Nova quantidade: "))
    except ValueError:
        print("Entrada inválida. Use números inteiros.")
        return

    for insumo in Estoque:
        if insumo["id"] == id_insumo:
            insumo["quantidade"] = nova_quantidade
            print(f"Insumo com ID {id_insumo} atualizado com sucesso.")
            return

    print("ID não encontrado.")

# Gera um relatório de insumos em um local específico
# Complexidade: O(n) - percorre todo o estoque
def RelatorioLocal():
    local_desejado = input("Digite o nome do local para o relatório: ")
    encontrou = False

    print(f"\n--- Relatório do Local: {local_desejado} ---")
    for insumo in Estoque:
        if insumo["local"].lower() == local_desejado.lower():
            encontrou = True
            print(f"ID: {insumo['id']}")
            print(f"Nome: {insumo['nome']}")
            print(f"Quantidade: {insumo['quantidade']}")
            print(f"Ideal: {insumo['ideal']}")
            print("-" * 30)

    if not encontrou:
        print("Nenhum insumo encontrado para esse local.")

# Exibe todos os insumos
# Complexidade: O(n)
def ExibirEstoque():
    if not Estoque:
        print("Estoque vazio.")
        return

    print("\n--- Estoque Atual ---")
    for insumo in Estoque:
        print(f"ID: {insumo['id']}")
        print(f"Nome: {insumo['nome']}")
        print(f"Local: {insumo['local']}")
        print(f"Quantidade: {insumo['quantidade']}")
        print(f"Ideal: {insumo['ideal']}")
        print("-" * 30)

# Busca insumos com base em campo e valor, usando ordenação e busca binária
def BuscarInsumo():
    if not Estoque:
        print("Estoque vazio.")
        return

    campos_validos = ["id", "nome", "local", "quantidade", "ideal"]
    campo = input(f"Digite o campo para buscar ({', '.join(campos_validos)}): ").lower()

    if campo not in campos_validos:
        print("Campo inválido.")
        return

    valor = input(f"Digite o valor para buscar no campo '{campo}': ")
    if campo in ["id", "quantidade", "ideal"]:
        try:
            valor = int(valor)
        except ValueError:
            print("Valor deve ser um número inteiro.")
            return

    # Ordena estoque pelo campo escolhido
    ordenados = sorted(Estoque, key=lambda ins: ins[campo])

    # Busca binária
    inicio = 0
    fim = len(ordenados) - 1
    achou = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if ordenados[meio][campo] == valor:
            achou = meio
            break
        elif ordenados[meio][campo] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1

    if achou == -1:
        print("Nenhum insumo encontrado com esse valor.")
        return

# Exibe todos os insumos com o mesmo valor (duplicatas consecutivas)
    print(f"\nInsumos com {campo} igual a '{valor}':")
    i = achou
    while i >= 0 and ordenados[i][campo] == valor:
        i -= 1
    i += 1

    while i < len(ordenados) and ordenados[i][campo] == valor:
        ins = ordenados[i]
        print(f"ID: {ins['id']}")
        print(f"Nome: {ins['nome']}")
        print(f"Local: {ins['local']}")
        print(f"Quantidade: {ins['quantidade']}")
        print(f"Ideal: {ins['ideal']}")
        print("-" * 30)
        i += 1

# Menu principal para interação com o sistema
# Executa em loop até o usuário escolher sair
while True:
    acao = input('''
    -- Gerenciador de Estoque Hospitalar --

    Digite o número da ação desejada:
    1 - Inserir Insumo
    2 - Exibir Insumo Mais Urgente (em falta)
    3 - Atualizar Quantidade de Insumo
    4 - Ver Relatório de um Local
    5 - Exibir Todo o Estoque
    6 - Buscar Insumo
    7 - Sair
    ''')

    try:
        numero = int(acao)

        if numero == 1:
            InserirInsumo()
        elif numero == 2:
            ProximoInsumoEmFalta()
        elif numero == 3:
            AtualizarQuantidade()
        elif numero == 4:
            RelatorioLocal()
        elif numero == 5:
            ExibirEstoque()
        elif numero == 6:
            BuscarInsumo()
        elif numero == 7:
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")

    except ValueError:
        print("Entrada inválida.")
