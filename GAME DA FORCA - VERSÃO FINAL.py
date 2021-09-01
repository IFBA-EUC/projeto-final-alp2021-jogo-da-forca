#!/usr/bin/env python
# coding: utf-8

# In[5]:





# In[ ]:


import random

vocabulario_easy = ['caneta', 'cadeira', 'xicara', 'colher', 'computador', 'celular', 'travesseiro', 'sapato', 'borracha', 'livro', 'escova', 'jarro', 'garfo', 'prato', 'panela', 'televisao', 'caderno', 'boneca', 'fronha', 'chaveiro', 'cachorro', 'gato', 'tigre', 'pato', 'caracol', 'tatu', 'ovelha', 'galinha', 'peixe', 'coelho', 'borboleta', 'vaca', 'elefante', 'ema', 'ganso', 'papagaio', 'formiga', 'coruja', 'tatu', 'tartaruga', 'cereja', 'goiaba', 'abacaxi', 'abacate', 'ameixa', 'uva', 'coco', 'figo', 'framboesa', 'umbu', 'jabuticaba', 'kiwi', 'laranja', 'melancia', 'morango', 'manga', 'seriguela', 'tangerina', 'banana', 'jenipapo']
vocabulario_normal = ['vitrola', 'dardo', 'alfinete', 'filmadora', 'abajur', 'frigideira', 'funil', 'foice', 'escudo', 'espiral', 'grampeador', 'gangorra', 'harpa', 'ampulheta', 'candelabro', 'desfibrilador', 'esparadrapo', 'marimba', 'quadriciclo', 'trampolim', 'coala', 'alce', 'flamingo', 'esquilo', 'ganso', 'jabuti', 'mariposa', 'pinguim', 'pulga', 'raposa',  'tucano', 'urubu', 'veado', 'formiga', 'corvo', 'coruja', 'cupim', 'girafa',  'iguana', 'jumento', 'amora', 'atemoia', 'gabiroba', 'groselha', 'ibacurupari', 'jaca', 'tamarindo', 'lima', 'mirtilo', 'murici', 'oiti', 'pinha', 'pequi', 'pistache', 'sapoti', 'acerola', 'graviola', 'castanha', 'ameixa', 'damasco']
vocabulario_hard = ['walkman', 'interruptor', 'fouet', 'termostato', 'daguerreotipo', 'compressor', 'condensador', 'xilogravura', 'pistoes', 'virabrequim', 'otoscopio', 'oftalmoscopio', 'laringoscopio', 'fluxometro', 'nebulizador', 'joystick', 'almofariz', 'astrolabio', 'bumerangue', 'ictiômetro', 'lince', 'jaguatirica', 'ariranha', 'guepardo', 'marsupiais', 'curimbata', 'corvina', 'jacutinga', 'orangotango', 'albatroz', 'antilope', 'urutaurana', 'chimpanze', 'guaxinim', 'iguanara', 'jacurupa', 'numbat', 'ornitorrinco', 'quatimirim', 'salamandra', 'abiu', 'alfarroba', 'araticum', 'beriba', 'buriti', 'cranberry', 'hilocereo', 'embauba', 'escropari', 'feijoa', 'gabiroba', 'imbe', 'jaraticaia', 'lichia', 'mabolo', 'macadamia', 'murici', 'naranjilla', 'pixirica', 'pistache']

objetos_easy = ['caneta', 'cadeira', 'xicara', 'colher', 'computador', 'celular', 'travesseiro', 'sapato', 'borracha', 'livro', 'escova', 'jarro', 'garfo', 'prato', 'panela', 'televisao', 'caderno', 'boneca', 'fronha', 'chaveiro']
objetos_hard = ['walkman', 'interruptor', 'fouet', 'termostato', 'daguerreotipo', 'compressor', 'condensador', 'xilogravura', 'pistoes', 'virabrequim', 'otoscopio', 'oftalmoscopio', 'laringoscopio', 'fluxometro', 'nebulizador', 'joystick', 'almofariz', 'astrolabio', 'bumerangue', 'ictiômetro']
objetos_normal= ['vitrola', 'dardo', 'alfinete', 'filmadora', 'abajur', 'frigideira', 'funil', 'foice', 'escudo', 'espiral', 'grampeador', 'gangorra', 'harpa', 'ampulheta', 'candelabro', 'desfibrilador', 'esparadrapo', 'marimba', 'quadriciclo', 'trampolim']

animais_easy = ['cachorro', 'gato', 'tigre', 'pato', 'caracol', 'tatu', 'ovelha', 'galinha', 'peixe', 'coelho', 'borboleta', 'vaca', 'elefante', 'ema', 'ganso', 'papagaio', 'formiga', 'coruja', 'tatu', 'tartaruga'] 
animais_hard = ['lince', 'jaguatirica', 'ariranha', 'guepardo', 'marsupiais', 'curimbata', 'corvina', 'jacutinga', 'orangotango', 'albatroz', 'antilope', 'urutaurana', 'chimpanze', 'guaxinim', 'iguanara', 'jacurupa', 'numbat', 'ornitorrinco', 'quatimirim', 'salamandra']
animais_normal = ['coala', 'alce', 'flamingo', 'esquilo', 'ganso', 'jabuti', 'mariposa', 'pinguim', 'pulga', 'raposa',  'tucano', 'urubu', 'veado', 'formiga', 'corvo', 'coruja', 'cupim', 'girafa',  'iguana', 'jumento']

frutas_easy = ['cereja', 'goiaba', 'abacaxi', 'abacate', 'ameixa', 'uva', 'coco', 'figo', 'framboesa', 'umbu', 'jabuticaba', 'kiwi', 'laranja', 'melancia', 'morango', 'manga', 'seriguela', 'tangerina', 'banana', 'jenipapo']
frutas_hard = ['abiu', 'alfarroba', 'araticum', 'beriba', 'buriti', 'cranberry', 'hilocereo', 'embauba', 'escropari', 'feijoa', 'gabiroba', 'imbe', 'jaraticaia', 'lichia', 'mabolo', 'macadamia', 'murici', 'naranjilla', 'pixirica', 'pistache']
frutas_normal = ['amora', 'atemoia', 'gabiroba', 'groselha', 'ibacurupari', 'jaca', 'tamarindo', 'lima', 'mirtilo', 'murici', 'oiti', 'pinha', 'pequi', 'pistache', 'sapoti', 'acerola', 'graviola', 'castanha', 'ameixa', 'damasco']

restart_config = ['s', 'n', 'config','r']
tema_dif = [1, 2, 3, 4]
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
palavras_sorteada = []
tentativas = []
respostas = []
chances = 7
chances1 = 7
chances2 = 7
vit1 = 0
der1 = 0
vit2 = 0
der2 = 0
troca = 0

print('Imprimindo as regras....')
print('\n')
print('- REGRAS DO JOGO DA FORCA -\n- O jogador/jogadores tem como objetivo adivinhar a palavra secreta em questão. Para que isso aconteça, é necessário que se\n chute determinadas vezes as letras que desejar.\n- A quantidade de chutes variam de acordo com a quantidade de letras e quantas vezes essas se repetem na palavra da vez.\n- Nessa versão, há a opção \nMultiplayer, onde mais de um indivíduo poderão jogar ao mesmo tempo. Jogar sozinho ou com um\n parceiro, será resultado de uma escolha sua.\n - Na opção Multiplayer, a vez de chute será alternada entre os jogadores, mas há um porém! A opção de chute só fará a troca após um erro, enquanto o jogador da vez acertar as letras presentes na palavra, poderá continuar inserindo mais e mais vezes até essa estar completa.\n- A cada chute (letra) errada, uma parte do boneco será desenhado na forca que aparecerá em sua tela.\n- Se o boneco for completamente desenhado antes da palavra ser desvendada, a partida será encerrada. Caso esteja na opção Multiplayer, a vitória será contabilizada para o jogador que não tiver seu boneco completo ainda.\n- A partir do 10° chute, ambos/o jogador, terá a opção de dizer a palavra completa caso saiba, se essa for adivinhada, a \npartida encerra-se alí mesmo e o placar com vencedor e perdedor aparecerá. Se o jogador/jogadores ainda não souber(em)\n a palavra secreta em questão, podem descartar a função e continuar a partida.\n- O jogador poderá inserir uma palavra de sua preferência se assim desejar, mas essa terá uma chance aleatória de ser usada\n na partida da vez.\n- Se o jogador desejar fazer modificações no jogo (isso incluí tema, nível de dificuldade e a escolha de uma partida solo ou Multiplayer, antes selecionada), pode! Porém o seu placar será resetado.\n- Há palavra secretas no jogo que possuem assento, porém, na hora das partidas não é necessário acentuá-las, o jogo rodará e considerará como certo sem os acentos.\n')
def bemvindo():    
    print("---------------------------")
    print("Bem vindo ao jogo da Forca!")
    print("---------------------------")
bemvindo()

def carrega_palavra1():
    if dificuldade == 1:
        palavra_secreta = random.choice(vocabulario_easy)
        while palavra_secreta in respostas:
            palavra_secreta = random.choice(vocabulario_easy)
        palavras_sorteada.append(palavra_secreta)
    elif dificuldade == 2:
        palavra_secreta = random.choice(vocabulario_normal)
        while palavra_secreta in respostas:
            palavra_secreta = random.choice(vocabulario_normal)
        palavras_sorteada.append(palavra_secreta)
    elif dificuldade == 3:
        palavra_secreta = random.choice(vocabulario_hard)
        while palavra_secreta in respostas:
            palavra_secreta = random.choice(vocabulario_hard)
        palavras_sorteada.append(palavra_secreta)
    return palavra_secreta
def carrega_palavra2():
    if dificuldade == 1:
        palavra_secreta = random.choice(animais_easy)
        while palavra_secreta in respostas:
            palavra_secreta = random.choice(animais_easy)
        palavras_sorteada.append(palavra_secreta)
    elif dificuldade == 2:
        palavra_secreta = random.choice(animais_normal)
        while palavra_secreta in respostas:
            palavra_secreta = random.choice(animais_normal)
        palavras_sorteada.append(palavra_secreta)
    elif dificuldade == 3:
        palavra_secreta = random.choice(animais_hard)
        while palavra_secreta in respostas:
            palavra_secreta = random.choice(animais_hard)
        palavras_sorteada.append(palavra_secreta)
    return palavra_secreta
def carrega_palavra3():
    if dificuldade == 1:
        palavra_secreta = random.choice(frutas_easy)
        while palavra_secreta in respostas:
            palavra_secreta = random.choice(frutas_easy)
        palavras_sorteada.append(palavra_secreta)
    elif dificuldade == 2:
        palavra_secreta = random.choice(frutas_normal)
        while palavra_secreta in respostas:
            palavra_secreta = random.choice(frutas_normal)
        palavras_sorteada.append(palavra_secreta)
    elif dificuldade == 3:
        palavra_secreta = random.choice(frutas_hard)
        while palavra_secreta in respostas:
            palavra_secreta = random.choice(frutas_hard)
        palavras_sorteada.append(palavra_secreta)
    return palavra_secreta
def carrega_palavra4():
    if dificuldade == 1:
        palavra_secreta = random.choice(objetos_easy)
        while palavra_secreta in respostas:
            palavra_secreta = random.choice(objetos_easy)
        palavras_sorteada.append(palavra_secreta)
    elif dificuldade == 2:
        palavra_secreta = random.choice(objetos_normal)
        while palavra_secreta in respostas:
            palavra_secreta = random.choice(objetos_normal)
        palavras_sorteada.append(palavra_secreta)
    elif dificuldade == 3:
        palavra_secreta = random.choice(objetos_hard)
        while palavra_secreta in respostas:
            palavra_secreta = random.choice(objetos_hard)
        palavras_sorteada.append(palavra_secreta)
    return palavra_secreta

        
def victory():
    print("Você venceu o jogo, parabéns")
    print("       _      ")
    print("      '.=====.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         .' '.        ")
    print("        '-------'       ")
    
def lost():
    print("Suas chances acabaram, eroooou!")
    print("A palavra era {}".format(palavra))
    print("    _         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("         \___/           ")

multi = str(input('Para jogar multiplayer digite:\nS para sim\nN para sou um pouco antisocial, então não\n')).lower()
if multi == 's':
    print('\n')
    pass
elif multi == 'n':
    print('\n')
    pass
else:
    multi = str(input('É "S" ou "N", como você se perde tendo apenas duas opções?:\nS para sim\nN para não\n')).lower()
    print('\n')
tema = int(input('Qual será o tema do jogo? Digite:\n1 para aleatório\n2 para animais\n3 para frutas\n4 para objetos.\n'))
print('\n')
while tema not in tema_dif:
    tema = int(input('Desculpe, humilde mestre, mas só temos 4 opções! Digite:\n1 para aleatório\n2 para animais\n3 para frutas\n4 para objetos.\n'))
    print('\n')
dificuldade = int(input('Qual a dificuldade você quer jogar? pode ser alterado no menu do jogo depois\n1 para easy\n2 para normal\n3 para hard\n'))
print('\n')
while dificuldade not in tema_dif:
    dificuldade = int(input('Essa não é uma das opções!\n1 para easy\n2 para normal\n3 para hard\n'))
    print('\n')
if dificuldade == 1:
    dificuldade_inter = 'Easy'
elif dificuldade == 2:
    dificuldade_inter = 'Medium'
elif dificuldade == 3:
    dificuldade_inter = 'Hard'
def new_word_def():
    new_word_config = str(input('Você gostaria de adicionar uma palavra ao jogo? a mesmo pode ser sorteada aleatoriamente\nS para sim\nN para não\n')).lower()
    print('\n')
    while new_word_config not in restart_config:
        new_word_config = str(input('Você gostaria de adicionar uma palavra ao jogo? a mesmo pode ser sorteada aleatoriamente\nS para sim\nN para não\n')).lower()
        print('\n')
    if new_word_config == 's':
        print('\n')
        while new_theme not in tema_dif:
            new_theme = int(input('Qual será o tema da palavra? Digite:\n1 para aleatório\n2 para animais\n3 para frutas\n4 para objetos.\n'))
            print('\n')
        new = str(input('Escreva aqui a palavra:\n'))
        print('\n')
        if len(new) >= 8:
            new_word_sugestão_hard = ''
            new_word_sugestao_hard = str(input('Detectamos que essa palavra possa ser um pouco difícil, deseja adiciona-lá na categoria hard?\nS para sim\nN para não\n')).lower()
            print('\n')
            while new_word_sugestao_hard not in restart_config:
                new_word_sugestao_hard = str(input('Detectamos que essa palavra possa ser um pouco difícil, deseja adiciona-lá na categoria hard?\nS para sim\nN para não\n')).lower() 
                print('\n')
            if new_word_sugestão_hard == 's':
                if new_theme == 1:
                    vocabulario_hard.append(new)
                elif new_theme == 2:
                    animais_hard.append(new)
                elif new_theme == 3:
                    frutas_hard.append(new)
                elif new_theme == 4:
                    objetos_hard.append(new)
            elif new_word_sugestão_hard == 'n':
                pass
        else:
            new_difficulty = int(input('Qual a dificuldade da palavra?\n1 para easy\n2 para normal\n3 para hard\n'))
            print('\n')
            while new_difficulty not in tema_dif:
                new_difficulty = int(input('Qual a dificuldade da palavra?\n1 para easy\n2 para normal\n3 para hard\n'))
                print('\n')
            if new_theme == 1:
                if new_difficulty == 1:
                    vocabulario_easy.append(new)
                elif new_difficulty == 2:
                    vocabulario_normal.append(new)                               
                elif new_difficulty == 3:
                    vocabulario_hard.append(new)            
            if new_theme == 2:
                if new_difficulty == 1:
                    animais_easy.append(new)
                elif new_difficulty == 2:
                    animais_normal.append(new)                               
                elif new_difficulty == 3:
                    animais_hard.append(new)                        
                                           
            if new_theme == 3:
                if new_difficulty == 1:
                    frutas_easy.append(new)
                elif new_difficulty == 2:
                    frutas_normal.append(new)                               
                elif new_difficulty == 3:
                    frutas_hard.append(new)
            if new_theme == 4:
                if new_difficulty == 1:
                    objetos_easy.append(new)
                elif new_difficulty == 2:
                    objetos_normal.append(new)                               
                elif new_difficulty == 3:
                    objetos_hard.append(new)
            new_theme = int(input('Qual será o tema da palavra? Digite:\n1 para aleatório\n2 para animais\n3 para frutas\n4 para objetos.\n'))
            print('\n')
                                       
restart = 0



while True:
    if tema == 1:
        tema_inter = 'Aleatório'
        while restart == 0:
            carrega_palavra1()
            del tentativas[:]
            chances = 7
            chances1 = 7
            chances2 = 7
            restart += 1      
            palavra = palavras_sorteada[0]
            respostas.append(palavra)
            palavras_sorteada.pop(0)
    elif tema == 2:
        tema_inter = 'Animais'
        while restart == 0:
            carrega_palavra2()
            del tentativas[:]
            chances = 7
            chances1 = 7
            chances2 = 7
            restart += 1      
            palavra = palavras_sorteada[0]
            respostas.append(palavra)
            palavras_sorteada.pop(0)
    elif tema == 3:
        tema_inter = 'Frutas'
        while restart == 0:
            carrega_palavra3()
            del tentativas[:]
            chances = 7
            chances1 = 7
            chances2 = 7
            restart += 1      
            palavra = palavras_sorteada[0]
            respostas.append(palavra)
            palavras_sorteada.pop(0)
    if tema == 4:
        tema_inter = 'Objetos'
        while restart == 0:
            carrega_palavra4()
            del tentativas[:]
            chances = 7
            chances1 = 7
            chances2 = 7
            restart += 1      
            palavra = palavras_sorteada[0]
            respostas.append(palavra)
            palavras_sorteada.pop(0)
    
    print('°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°')
    print('\n')
    print('O tema é: {}'.format(tema_inter))
    print('Você está jogando na dificuldade: {}'.format(dificuldade_inter))
    print('Tentativas:', tentativas)
    print('\n')
    if multi == 'n':
        print('Chances:', chances)
        print('\n')
    elif multi == 's':
        print('Chances do Jogador 1:', chances1)
        print('Chances do Jogador 2:', chances2)
        print('\n')
    if multi == 'n':
        print('\nVocê está com {0} vitórias e {1} derrotas'.format(vit1, der1))
    elif multi == 's':
        print('\nO jogador 1 está com {0} vitórias e {1} derrotas\nO jogador 2 está com {2} vitórias e {3} derrotas'.format(vit1, der1, vit2, der2))
        if troca == 0: 
            print('Essa é a vez do jogador 1\n')
        else:
            print('Essa é a vez do jogador 2\n')
       
    for letras in palavra:
        if letras in tentativas:
            print(letras, end=' ')
        else:
            print('_', end=' ')
    print('\n')        
    print('\n°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°\n')            
    
    def desenha_forca():
        print("  _     ")
        print(" |/      |    ")
        if(chances == 6):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if(chances == 5):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if(chances == 4):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if(chances == 3):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if(chances == 2):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if(chances == 1):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")
 
        if (chances == 0):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

            print(" |            ")
            print("|__         ")
            print()
    def desenha_forca1():
        print("  _     ")
        print(" |/      |    ")
        if(chances1 == 6):
            print(" |     (o-o)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if(chances1 == 5):
            print(" |     (o-o)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if(chances1 == 4):
            print(" |     (o-o)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if(chances1 == 3):
            print(" |     (o-o)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if(chances1 == 2):
            print(" |     (o-o)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if(chances1 == 1):
            print(" |     (o-o)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")
 
        if (chances1 == 0):
            print(" |     (o-o)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

            print(" |            ")
            print("|__         ")
            print()
    def desenha_forca2():
        print("  _     ")
        print(" |/      |    ")
        if(chances2 == 6):
            print(" |     (<o>)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if(chances2 == 5):
            print(" |     (<o>)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if(chances2 == 4):
            print(" |     (<o>)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if(chances2 == 3):
            print(" |     (<o>)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if(chances2 == 2):
            print(" |     (<o>)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if(chances2 == 1):
            print(" |     (<o>)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")
 
        if (chances2 == 0):
            print(" |     (<o>)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

            print(" |            ")
            print("|__         ")
            print()        
    
    
    chute = str(input('\nDigite uma letra ou escreva "SAIR" para sair do jogo ou "CONFIG" para acessar as configurações\n')).lower()
    if chute == 'config':
        config_option = str(input('Opa, se arrependeu do que escolheu no inicio não é?\nQuer alterar o modo de jogo?\nS para sim\nN para não\n')).lower()
        print('\n')
        while config_option not in restart_config:
            config_option = str(input('Eu não sou tão paciente assim, se decida!\nQuer alterar o modo de jogo?\nS para sim\nN para não\n')).lower()
            print('\n')
        if config_option == 's': 
            multi = str(input('Para jogar multiplayer digite:\nS para sim\nN para sou um pouco antisocial, então não\n')).lower()
            print('\n')
            if multi == 's':
                pass
            elif multi == 'n':
                pass
            else:
                multi = str(input('É "S" ou "N", como você se perde tendo apenas duas opções?:\nS para sim\nN para não\n')).lower()
                print('\n')
            tema = int(input('Qual será o tema do jogo? Digite:\n1 para aleatório\n2 para animais\n3 para frutas\n4 para objetos.\n'))
            print('\n')
            while tema not in tema_dif:
                tema = int(input('Desculpe, humilde mestre, mas só temos 4 opções! Digite:\n1 para aleatório\n2 para animais\n3 para frutas\n4 para objetos.\n'))
                print('\n')
            dificuldade = int(input('Qual a dificuldade você quer jogar? pode ser alterado no menu do jogo depois\n1 para easy\n2 para normal\n3 para hard\n'))
            print('\n')
            while dificuldade not in tema_dif:
                dificuldade = int(input('Essa não é uma das opções!\n1 para easy\n2 para normal\n3 para hard\n'))
                print('\n')
            if dificuldade == 1:
                dificuldade_inter = 'Easy'
            elif dificuldade == 2:
                dificuldade_inter = 'Medium'
            elif dificuldade == 3:
                dificuldade_inter = 'Hard'
            new_word_def()
            chances = 7
            chances1 = 7
            chances2 = 7   
            restart = 0
            chute = str(input('\nDigite "R" para reinicar com as respectivas alterações\n')).lower()
            print('\n')
            while chute != 'r':
                chute = str(input('\nPara confirmar o comando Digite especificamente a letra "R"\n')).lower()
                print('\n')
        elif config_option == 'n':
            pass                                                                                   
    elif chute == 'sair':
        break
        vit1 = 0
        der1 = 0
        vit2 = 0
        der2 = 0
    elif chute not in alfabeto:
        print("Parece que você não sabe o que UMA letra é, tente novamente\n")
        print('\n')
    elif chute != 'config':
        while chute not in alfabeto or len(chute) > 1:
            chute = str(input('\nDigite uma letra ou escreva "SAIR" para sair do jogo\n')).lower()
            print('\n')
            if chute == 'sair':
                del respostas[:]
                vit1 = 0
                der1 = 0
                vit2 = 0
                der2 = 0
                break
    if chute in tentativas:
        print("Você já chutou essa letra, o alzheimer ta forte\n")
        print('\n')
    elif chute in palavra:
        print("Parabéns, essa letra aparece na palavra secreta\n")
        print('\n')
        if troca == 0:
            troca = 0
        else:
            troca = 1
        tentativas.append(chute)
    elif chute not in palavra or restart_config or tentativas:
        print("Essa letra não faz parte da palavra secreta\n")
        print('\n')
        if multi == 'n':
            chances -= 1
            desenha_forca()
        else:
            if troca == 0:
                chances1 -=1
                desenha_forca1()
                troca = 1
            else:
                chances2 -=1
                desenha_forca2()
                troca = 0
        tentativas.append(chute)  
    if len(tentativas) > 10:
        palpite = str(input('Quer chutar a palavra? isso é um ultimato\nS para sim\nN para não\n')).lower()
        print('\n')
        while palpite not in restart_config:
            palpite = str(input('Quer chutar a palavra? isso é um ultimato\nS para sim\nN para não\n')).lower()
            print('\n')
        if palpite == 's':
            palpite_true = str(input('Chute a palavra:\n')).lower()
            print('\n')
            if palpite_true == palavra:
                victory()
                if multi == 'n':
                    vit1 += 1
                elif multi == 's':
                    if troca == 0:
                        vit1 +=1
                        print('O jogador 1 venceu essa rodada')
                    else:
                        vit2 +=1
                        print('O jogador 2 venceu essa rodada')
                loop = str(input('Quer jogar novamente? Digite:\nS para sim\nN para não\n')).lower()
                print('\n')
                while loop not in restart_config:
                    loop = str(input('Eu não sei ler mentes! Digite:\nS para sim\nN para não\n')).lower()
                    print('\n')
                if loop == 's':
                    chances = 7
                    chances1 = 7
                    chances2 = 7
                    restart = 0     
                elif loop == 'n':
                    del respostas[:]
                    break
                
            elif palpite_true != palpite:
                if multi == 's':
                    print('Eu te dei a chance, você errou e será penalizado\n')
                    print('\n')
                    if troca == 0:
                        chances1 -=1
                        desenha_forca1()
                    else:
                        chances2 -=1
                        desenha_forca2()
                else:
                    chances -=1
                    desenha_forca()
        if palpite == 'n':
            print('Então tá, boa sorte')
            print('\n')
            pass
    if chances == 0:
        print('Você perdeu!')
        print('\n')
        lost()
        der1 +=1
        loop = str(input('Quer jogar novamente? Digite:\nS para sim\nN para não\n')).lower()
        print('\n')
        while loop not in restart_config:
            loop = str(input('Eu não sei ler mentes! Digite:\nS para sim\nN para não\n')).lower()
            print('\n')
        if loop == 's':
            chances = 7
            chances1 = 7
            chances2 = 7
            restart = 0     
        elif loop == 'n':
            del respostas[:]
            if multi == 'n':
                print('\nVocê está com {0} vitórias e {1} derrotas'.format(vit1, der1))
                print('\n')
            elif multi == 's':
                print('\nO jogador 1 terminou o jogo com {0} vitórias e {1} derrotas\nO jogador 2 terminou o jogo com {2} vitórias e {3} derrotas'.format(vit1, der1, vit2, der2))
                print('\n')
                if vit1 > vit2 or der1 < der2:
                    print('O jogador 1 venceu o jogador 2')
                elif vit1 == vit2:
                    print('Os jogadores empataram')
                else:
                    print('O jogador 2 venceu o jogador 1')
                    vit1 = 0
                    der1 = 0
                    vit2 = 0
                    der2 = 0
                    break
    elif chances1 == 0:
        print('O jogador 1 pereceu')
        print('\n')
        lost()
        der1 +=1
        loop = str(input('Quer jogar novamente? Digite:\nS para sim\nN para não\n')).lower()
        print('\n')
        while loop not in restart_config:
            loop = str(input('Eu não sei ler mentes! Digite:\nS para sim\nN para não\n')).lower()
            print('\n')
        if loop == 's':
            chances = 7
            chances1 = 7
            chances2 = 7
            restart = 0     
        elif loop == 'n':
            del respostas[:]
            if multi == 'n':
                print('\nVocê está com {0} vitórias e {1} derrotas'.format(vit1, der1))
                print('\n')
            elif multi == 's':
                print('\nO jogador 1 terminou o jogo com {0} vitórias e {1} derrotas\nO jogador 2 terminou o jogo com {2} vitórias e {3} derrotas'.format(vit1, der1, vit2, der2))
                print('\n')
                if vit1 > vit2 or der1 < der2:
                    print('O jogador 1 venceu o jogador 2')
                elif vit1 == vit2:
                    print('Os jogadores empataram')
                else:
                    print('O jogador 2 venceu o jogador 1')
                    vit1 = 0
                    der1 = 0
                    vit2 = 0
                    der2 = 0
                    break
    elif chances2 == 0:
        print('O jogador 2 pereceu')
        print('\n')
        lost()
        der2 +=1
        loop = str(input('Quer jogar novamente? Digite:\nS para sim\nN para não\n')).lower()
        print('\n')
        while loop not in restart_config:
            loop = str(input('Eu não sei ler mentes! Digite:\nS para sim\nN para não\n')).lower()
            print('\n')
        if loop == 's':
            chances = 7
            chances1 = 7
            chances2 = 7
            restart = 0
            
        elif loop == 'n':
            del respostas[:]
            if multi == 'n':
                print('\nVocê está com {0} vitórias e {1} derrotas'.format(vit1, der1))
            elif multi == 's':
                print('\nO jogador 1 terminou o jogo com {0} vitórias e {1} derrotas\nO jogador 2 terminou o jogo com {2} vitórias e {3} derrotas'.format(vit1, der1, vit2, der2))
                print('\n')
                if vit1 > vit2 or der1 < der2:
                    print('O jogador 1 venceu o jogador 2')
                elif vit1 == vit2:
                    print('Os jogadores empataram')
                else:
                    print('O jogador 2 venceu o jogador 1')
                    vit1 = 0
                    der1 = 0
                    vit2 = 0
                    der2 = 0
                    break
    elif set(palavra).issubset(set(tentativas)):
        victory()
        if multi == 'n':
            vit1 += 1
        elif multi == 's':
            if troca == 0:
                vit1 +=1
                print('O jogador 1 venceu essa rodada')
            else:
                vit2 +=1
                print('O jogador 2 venceu essa rodada')
        loop = str(input('Quer jogar novamente? Digite:\nS para sim\nN para não\n')).lower()
        print('\n')
        while loop not in restart_config:
            loop = str(input('Eu não sei ler mentes! Digite:\nS para sim\nN para não\n')).lower()
            print('\n')
        if loop == 's':
            chances = 7
            chances1 = 7
            chances2 = 7
            restart = 0     
        elif loop == 'n':
            del respostas[:]
            if multi == 'n':
                print('\nVocê está com {0} vitórias e {1} derrotas'.format(vit1, der1))
                print('\n')
        elif multi == 's':
                print('\nO jogador 1 terminou o jogo com {0} vitórias e {1} derrotas\nO jogador 2 terminou o jogo com {2} vitórias e {3} derrotas'.format(vit1, der1, vit2, der2))
                print('\n')
                if vit1 > vit2 or der1 < der2:
                    print('O jogador 1 venceu o jogador 2')
                elif vit1 == vit2:
                    print('Os jogadores empataram')
                else:
                    print('O jogador 2 venceu o jogador 1')
                vit1 = 0
                der1 = 0
                vit2 = 0
                der2 = 0
                break


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




