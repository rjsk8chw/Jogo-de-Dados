
import random



def lancamento():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    return d1, d2


def relacao(d1, d2):
    if d1 > d2:
        return f'{d1} é maior que {d2} ...jogador 1 venceu...'

    elif  d1 == d2:
        return f'VALORES IGUAIS!!'
    else:
        return f'{d2} é maior que {d1} ...jogador 2 venceu...'


print('##############    JOGO DE DADOS ###################')
print('REGRAS: DOIS DADOS SERÃO LANÇADOS O MAIOR VALOR VENCE, VOCÊ ESCOLHE O NUMERO DE LANÇAMENTOS, QUEM TIRAR O MAIOR VALOR MAIS VEZES VENCE!')
print('###########################################################################################################')
n = int(input('lançar os dados qts vezes?'))
d1, d2 = lancamento()

for i in range (1, n + 1) :
    d1, d2 = lancamento()
    rel = relacao(d1, d2)
    print(f'{i} ° lançamento ==>> ({d1}, {d2}) =====>>>>  {rel}')


input('Digite enter para sair')


