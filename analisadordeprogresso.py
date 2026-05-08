from time import sleep
import os
import time

print('-=' *20)
print('      -=-= MONITOR DE PROJETOS =-=-')
print('-=' * 20)
sleep(1)

def exibir_progresso():
    print(' ')
    projeto = input('No que você está trabalhando agora? ')
    print(' ')
    progresso = int(input('De 0 a 100, quanto de {} já foi concluído? '.format(projeto)))

    tamanho_barra = 10  # (cada '#' representa 10%)
    blocos = progresso // 10
    barra = '[' + '#' * blocos + '-' * (tamanho_barra - blocos) + ']'

    os.system('cls' if os.name == 'nt' else 'clear')
    
    
    
    print(f'Projeto atual: {projeto}')
    print('-=' * 20)
    sleep(1)
    print(f'Progresso: {barra} {progresso}%')
    sleep(1)

    if progresso >= 100:
        print('-=' * 20)
        sleep(1)
        print('Concluído! Parabéns!')
        sleep(0.50)
        print('-=' * 20)
        print( '-=-= FIM DO PROGRAMA =-=-')
    elif progresso >= 50:
        print('-=' * 20)
        sleep(1)
        print('Metade já foi, falta pouco!')
        sleep(0.5)
        print('-=' * 20)
        print( '-=-= FIM DO PROGRAMA =-=-')
    else: 
        print('-=' * 20)
        sleep(1)
        print('No caminho certo, continue firme!')
        sleep(0.5)
        print('-=' * 20)
        print( '-=-= FIM DO PROGRAMA =-=-')

sleep(1)

exibir_progresso()
