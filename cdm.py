'''                                                                                      2. Conversor de Medidas
                                                 Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
                                                                            Dica: Lembre-se que $1m = 100cm$ e $1m = 1000mm$'''

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

'''n = float(input('Digite um número: '))
cm = n * 10  #aquiera100pracm
ml = n * 100 #aquiera1000ml
print(f'{n} são {cm} centímetros e {ml} milímetros ')'''

# --=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= v2.0

n = float(input('Digite um número: '))
print(f'{n}m equivale a {n * 100:.0f}cm e {n * 1000:.0f}mm')

