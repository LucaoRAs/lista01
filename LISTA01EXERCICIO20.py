moedasde1= int(input("Digite a quantidade de moedas de 1 centavo: "))
moedasde5= int(input("Digite a quantidade de moedas de 5 centavos: "))
moedasde10= int(input("Digite a quantidade de moedas de 10 centavos: "))
moedasde25= int(input("Digite a quantidade de moedas de 25 centavos: "))
moedasde50= int(input("Digite a quantidade de moedas de 50 centavos: "))
moedasde1real= int(input("Digite a quantidade de moedas de 1 real: "))

valort= moedasde1 * 0.01 + moedasde5 * 0.05 + moedasde10 * 0.1 + moedasde25 * 0.25 + moedasde50 * 0.5 + moedasde1real

print(f'O valor total economizado é de: R${valort}')

