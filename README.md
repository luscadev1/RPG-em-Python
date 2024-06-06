# Jogo de RPG em Python

Este é um simples jogo de RPG baseado em texto, onde os jogadores podem lutar contra NPCs (Non-Player Characters), ganhar experiência, subir de nível, coletar itens e usar esses itens para melhorar suas estatísticas.

## Funcionalidades

1. **Iniciar Batalha**: Inicia uma batalha entre o jogador e um NPC. Durante a batalha, o jogador e o NPC se revezam para atacar um ao outro até que um deles fique sem pontos de vida (HP). Se o jogador vencer, ele ganha experiência e um item.

2. **Exibir Itens**: Mostra os itens que o jogador possui e suas respectivas quantidades.

3. **Usar Item**: Permite ao jogador usar um item que possui. O item usado aumentará uma estatística específica do jogador (por exemplo, "poção de vida" aumenta o HP e "poção de força" aumenta o dano).

4. **Exibir Estatísticas**: Exibe as estatísticas atuais do jogador, incluindo nome, nível, dano, HP e experiência.

5. **Salvar Jogo**: Salva o estado atual do jogo em um arquivo chamado 'savegame.pkl'.

6. **Carregar Jogo**: Carrega o estado do jogo a partir do arquivo 'savegame.pkl'.

7. **Sair**: Sai do jogo.

## Como Jogar

Para jogar, execute o script Python e siga as instruções na tela. Você será solicitado a escolher uma opção do menu principal. Cada opção corresponde a uma funcionalidade diferente do jogo.

## Importações

O jogo usa os módulos `pickle` e `random`. `pickle` é usado para salvar e carregar o estado do jogo, enquanto `random` é usado para gerar números aleatórios para várias partes do jogo, como a criação de NPCs e a atribuição de itens.

## Contribuições

Contribuições para este projeto são bem-vindas! Se você encontrar um bug ou tem uma sugestão de melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request.

---

# Python RPG Game

This is a simple text-based RPG game where players can fight against NPCs (Non-Player Characters), gain experience, level up, collect items, and use these items to improve their stats.

## Features

1. **Start Battle**: Starts a battle between the player and an NPC. During the battle, the player and the NPC take turns attacking each other until one of them runs out of health points (HP). If the player wins, they gain experience and an item.

2. **Display Items**: Shows the items that the player has and their respective quantities.

3. **Use Item**: Allows the player to use an item they have. The used item will increase a specific stat of the player (for example, "life potion" increases HP and "strength potion" increases damage).

4. **Display Stats**: Displays the current stats of the player, including name, level, damage, HP, and experience.

5. **Save Game**: Saves the current state of the game to a file named 'savegame.pkl'.

6. **Load Game**: Loads the game state from the 'savegame.pkl' file.

7. **Exit**: Exits the game.

## How to Play

To play, run the Python script and follow the instructions on the screen. You will be prompted to choose an option from the main menu. Each option corresponds to a different feature of the game.

## Imports

The game uses the `pickle` and `random` modules. `pickle` is used to save and load the game state, while `random` is used to generate random numbers for various parts of the game, such as creating NPCs and assigning items.

## Contributions

Contributions to this project are welcome! If you find a bug or have a suggestion for improvement, feel free to open an issue or submit a pull request.

