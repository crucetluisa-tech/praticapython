
total_pontos = 0 

pontos = int(input('Quantos pontos você fez agora? [digite 0 pra encerrar]'))
    
while pontos != 0:
    total_pontos = total_pontos + pontos
    pontos = int(input('Quantos pontos você fez agora [digite 0 pra encerrar]'))
print('O seu placar foi de: {}'.format(total_pontos))

    

