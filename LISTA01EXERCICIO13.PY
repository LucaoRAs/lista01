VALORP= float(input('Preço do produto: '))
print(f'{VALORP}')
acresc= float(input('Quanto será acrescentado?'))
porcen= acresc/100
valort= VALORP*porcen
prod= valort+VALORP
print(f'O preço do produto é: {prod} ')
