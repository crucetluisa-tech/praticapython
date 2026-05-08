#1. O Contador de Erros (Nível Básico)
#Crie um programa que peça uma senha ao usuário.
#
#A lógica: Enquanto a senha digitada for diferente de "python123", o programa deve dizer "Acesso negado, tente novamente" e pedir a senha de novo.
#
#O objetivo: Só sair do loop quando ele acertar. No final, mostre "Acesso liberado!".


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=

senha = str(input('Senha: '))

while senha != 'python123':
    print('Acesso negado,')
    senha = str(input('tente novamente. '))

print('Acesso liberado!')


#algoerradoelenentraemloop