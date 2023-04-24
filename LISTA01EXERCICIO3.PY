valorFabrica= int(input('Qual o custo da fábrica? '))
Cfabrica= (valorFabrica*(28/100))
Cimposto= (valorFabrica*(45/100))
Cconsumidor= Cfabrica+Cimposto 
print(f'O valor que o consumidor irá pagar é:{Cconsumidor}')

