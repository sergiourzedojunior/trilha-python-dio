import textwrap

# Inicializa os usuários e contas diretamente no script para garantir que estão disponíveis.
usuarios = [
    {"nome": "Sergio", "cpf": "03217296680", "data_nascimento": "01-01-1980", "endereco": "Endereço de Sergio"}
]
contas = [
    {"id": 1, "agencia": "0001", "numero_conta": "12345", "usuario": usuarios[0], "saldo": 10000000, "extrato": "", "tipo": "Poupança"},
    {"id": 2, "agencia": "0001", "numero_conta": "54321", "usuario": usuarios[0], "saldo": 20000, "extrato": "", "tipo": "Corrente"}
]


def menu():
    return """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [tf]\tTransferir fundos
    [cs]\tMudar conta
    [q]\tSair
    => """

def exibir_menu_cliente(cpf):
    print(f"\nContas registradas para CPF {cpf}:")
    for conta in contas:
        if conta['usuario']['cpf'] == cpf:
            print(f"ID: {conta['id']}, Tipo: {conta['tipo']}, Saldo: R$ {conta['saldo']:.2f}")
    conta_selecionada_id = int(input("Selecione o ID da conta para operar: "))
    conta_selecionada = next((conta for conta in contas if conta['id'] == conta_selecionada_id and conta['usuario']['cpf'] == cpf), None)
    if conta_selecionada:
        print(f"Operando na conta ID {conta_selecionada['id']} do tipo {conta_selecionada['tipo']}.")
        return conta_selecionada
    else:
        print("Conta inválida ou não encontrada.")
        return None

def transferir_fundos(conta_origem):
    # Implementação da função de transferência de fundos.
    pass

def selecionar_acao(conta_ativa):
    while True:
        opcao = input(textwrap.dedent(menu()))
        if opcao == "q":
            break
        elif opcao == "cs":
            return "cs"
        # Implementar as outras opções de ação aqui.
        # Lembre-se de passar 'conta_ativa' para as funções que necessitam.
        elif opcao == "tf":
            transferir_fundos(conta_ativa)
        # Adicione as outras opções conforme necessário.

def main():
    cpf = input("Por favor, entre com seu CPF para acessar suas contas: ")
    conta_ativa = exibir_menu_cliente(cpf)
    while conta_ativa:
        resultado = selecionar_acao(conta_ativa)
        if resultado == "cs":
            conta_ativa = exibir_menu_cliente(cpf)
        elif not conta_ativa:
            break

if __name__ == "__main__":
    main()
