CONSTANTE_BONUS = 1000

nome = input("Digite seu nome: ")
salario = float(input("Digite seu salario: "))
bonus = float(input("Digite seu bonus: "))
kpi = CONSTANTE_BONUS + salario * bonus
print(f"Olá {nome}, o seu bônus foi de {kpi}")
