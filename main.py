import pickle
from random import randint

lista_npcs = []
lista_jogadores = []


itens = {
    "poção de vida": {"hp": 50},
    "poção de força": {"dano": 10},
}


def criar_jogador(nome):
    novo_jogador = {
        "nome": nome,
        "level": 1,
        "exp": 0,
        "exp_max": 30,
        "hp": 100,
        "hp_max": 100,
        "dano": 25,
        "itens": [],
    }
    return novo_jogador


def criar_npc(level):
    tipos = ["Monstro", "Dragão", "Zumbi"]
    tipo = tipos[randint(0, len(tipos)-1)]
    novo_npc = {
        "nome": f"{tipo} #{level}",
        "level": level,
        "dano": 5 * level,
        "hp": 100 * level,
        "hp_max": 100 * level,
        "exp": 7 * level,
    }
    return novo_npc


def gerar_npcs(n_npcs):
    for x in range(n_npcs):
        npc = criar_npc(x + 1)
        lista_npcs.append(npc)


def exibir_npcs():
    for npc in lista_npcs:
        exibir_npc(npc)


def exibir_npc(npc):
    print(
        f"Nome: {npc['nome']} // Level: {npc['level']} // Dano: {npc['dano']} // HP: {npc['hp']} // EXP: {npc['exp']}"
    )


def exibir_jogador(jogador):
    print(
        f"Nome: {jogador['nome']} // Level: {jogador['level']} // Dano: {jogador['dano']} // HP: {jogador['hp']}/{jogador['hp_max']} // EXP: {jogador['exp']}/{jogador['exp_max']}"
    )


def reset_jogador(jogador):
    jogador["hp"] = jogador["hp_max"]

def reset_npc(npc):
    npc["hp"] = npc["hp_max"]


def level_up(jogador):
    if jogador["exp"] >= jogador["exp_max"]:
        jogador["level"] += 1
        jogador["exp"] = 0
        jogador["exp_max"] = jogador["exp_max"] * 2
        jogador["hp_max"] += 20
        jogador["dano"] += 5  # Aumentar o dano quando subir de nível

def iniciar_batalha(jogador, npc):
    while jogador["hp"] > 0 and npc["hp"] > 0:
        atacar_npc(jogador, npc)
        atacar_jogador(jogador, npc)
        exibir_info_batalha(jogador, npc)

    if jogador["hp"] > 0:
        print(f"O {jogador['nome']} venceu e ganhou {npc['exp']} de EXP!")
        jogador["exp"] += npc["exp"]
        ganhar_item(jogador)  # Ganhar um item após a batalha
        exibir_jogador(jogador)
    else:
        print(f"O {npc['nome']} venceu!")
        exibir_npc(npc)

    level_up(jogador)
    reset_jogador(jogador)
    reset_npc(npc)

def atacar_npc(jogador, npc):
    npc["hp"] -= jogador["dano"]


def atacar_jogador(jogador, npc):
    jogador["hp"] -= npc["dano"]

def exibir_info_batalha(jogador, npc):
    print(f"Jogador: {jogador['hp']}/{jogador['hp_max']}")
    print(f"NPC: {npc['nome']}: {npc['hp']}/{npc['hp_max']}")
    print("-----------------\n")

def ganhar_item(jogador):
    item = list(itens.keys())[randint(0, len(itens)-1)]
    jogador["itens"].append(item)
    print(f"{jogador['nome']} ganhou um item: {item}!")

def usar_item(jogador, item):
    if item in jogador["itens"]:
        for stat, valor in itens[item].items():
            jogador[stat] += valor
        jogador["itens"].remove(item)
        print(f"{jogador['nome']} usou {item}!")
    else:
        print("Você não tem esse item.")

def salvar_jogo():
    with open('savegame.pkl', 'wb') as f:
        pickle.dump(lista_jogadores, f)
    print("Jogo salvo com sucesso!")

def carregar_jogo():
    global lista_jogadores
    with open('savegame.pkl', 'rb') as f:
        lista_jogadores = pickle.load(f)
    print("Jogo carregado com sucesso!")


def exibir_itens(jogador):
    if jogador["itens"]:
        print(f"{jogador['nome']} tem os seguintes itens:")
        for item in set(jogador["itens"]):
            quantidade = jogador["itens"].count(item)
            print(f"{item}: {quantidade}")
    else:
        print(f"{jogador['nome']} não tem itens.")

def menu_principal():
    while True:
        print("\n1. Iniciar batalha")
        print("2. Exibir itens")
        print("3. Usar item")
        print("4. Exibir estatísticas")
        print("5. Salvar jogo")
        print("6. Carregar jogo")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            npc_selecionado = lista_npcs[0]
            for jogador in lista_jogadores:
                iniciar_batalha(jogador, npc_selecionado)
        elif opcao == "2":
            jogador_selecionado = lista_jogadores[0]  # Selecionar o primeiro jogador por enquanto
            exibir_itens(jogador_selecionado)
        elif opcao == "3":
            jogador_selecionado = lista_jogadores[0]  # Selecionar o primeiro jogador por enquanto
            item = input("Digite o nome do item que você quer usar: ")
            usar_item(jogador_selecionado, item)
        elif opcao == "4":
            for jogador in lista_jogadores:
                exibir_jogador(jogador)
        elif opcao == "5":
            salvar_jogo()
        elif opcao == "6":
            carregar_jogo()
        elif opcao == "7":
            break
        else:
            print("Opção inválida!")


lista_jogadores.append(criar_jogador("Lucas"))
lista_jogadores.append(criar_jogador("Ana"))


gerar_npcs(5)

menu_principal()
