NOME= input('Seu nome: ')
Sf= float(input('Seu salário: '))
Tv= float(input('Total de vendas: '))
porc= Tv*15/100
ST= Sf + porc
print(f'{NOME} recebe um salário fixo de {Sf}, porém seu salário com a comissão é: {ST}')
