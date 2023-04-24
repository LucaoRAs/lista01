salarioincial= float(input('Qual o seu salário?: '))
aumento= (salarioincial*15/100) + salarioincial
imposto= salarioincial + (aumento*8/100)
print(f'Seu salário era: {salarioincial}, com o aumento de 15% foi para {aumento:.2f}, com o desconto do INSS de 8% seu salário agora é de: {imposto:.2f}.')