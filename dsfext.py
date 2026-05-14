'''                                                                                     Desafio Extra: O Par ou Ímpar
                                                             Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
                                              Dica: Em Python, o operador % (módulo) retorna o resto da divisão. Se um número dividido por 2 tiver resto 0, ele é par!'''

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= erradoalgoavercomoifetrueorfalse
'''n = int(input('digite um número: '))

if n % 2:
    print(f'{n} é PAR!')

elif n % 3:
    print(f'{n} é ÍMPAR!')''' 

'''
* == 0: Agora estamos perguntando explicitamente: "O resto da divisão por 2 é igual a zero?".
* else: Se a condição do if não for verdadeira, ele cai direto no else. Não precisa de outra conta matemática para saber que é ímpar.'''

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

n = int(input('Digite um número: '))

if n % 2 == 0:
    print(f'{n} é PAR! ')

else:
    print(f'{n} é ÍMPAR! ')