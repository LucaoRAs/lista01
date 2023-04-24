pao= 0.12
bolo= 1.50
quantidadeP= float(input('Quantidade de pães vendida:'))
quantidadeB= float(input('Quantidade de bolos vendida:'))
valorp= (pao*quantidadeP )
valorb= (quantidadeB*bolo)
print(f'Vendeu {quantidadeP} de pães que deu: {valorp:.2f}')
print(f'Vendeu {quantidadeB} de bolos que deu: {valorb:.2f}')

valort= valorp+valorb
print(f'Teve uma renda de {valort}')

guardar= valort*10/100

print(f'Você deve guardar: {guardar:.2f}')





