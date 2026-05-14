'''                                                                            A Tabuada Automática (for)
                                    Peça para o usuário digitar um número e, usando o laço for e a função range(), mostre a tabuada desse número de 1 a 10.
                                                                          Dica: O range(1, 11) vai do 1 até o 10.'''

n = int(input('Digite um número pra ver a sua tabuada: '))
for c in range (1, 11): 
    print(f'{n} x {c:2} = {n * c:2}')