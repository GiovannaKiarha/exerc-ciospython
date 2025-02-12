print('Seja bem vindo ao quiz da Giovanna!')

answer_user = input('Quer começar? (S/N)')

print(answer_user)

if answer_user != "S":
    quit() # encerra a execução do script

score = 0

print('Começando...')

print('Quem desenvolveu o jogo Overwatch 2? \n (A) Rockstar Games \n (B) Blizzard \n (C) Riot Games')
answer_1 = input('Reposta: ')

if answer_1 == 'B':
    print('Você acertou!')
    score = score + 1
else:
    print('Você errou')

print('Qual é o ano de lançamento de Overwatch? \n (A) 2016 \n (B) 2018 \n (C) 2020')
answer_2 = input('Resposta: ')

if answer_2 == 'A':
    print('Você acertou!')
    score = score + 1
else:
    print('Você errou')

print('Qual era o personagem da capa de Overwatch no lançamento? \n (A) Mercy \n (B) Tracer \n (C) WidowMaker')
answer_3 = input('Reposta: ')

if answer_3 == 'B':
    print('Você acertou!')
    score = score + 1
else:
    print('Você errou')

print(f'Quiz acabou... Pontuação: {score}/3')