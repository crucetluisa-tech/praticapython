'''                                                                                       1. O Dobro e a Terça Parte
                                                        Crie um programa que leia um número real e mostre na tela o seu dobro e a sua terça parte.
                                                                               Exemplo: Se digitar 9, o programa retorna 18 e 3.0.'''

n = int(input('Digite um número: '))
dobro = n * 2
tp = n / 3
print(f'O dobro de {n} é igual a {dobro}')
print(f'E sua terça parte é {tp:.2f}')
