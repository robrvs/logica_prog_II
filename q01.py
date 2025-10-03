# Solicita a quantidade de pessoas que moram na mesma casa
qtd = int(input("Digite a quantidade de pessoas que moram na mesma casa que você: "))

# Verifica se a quantidade é par ou ímpar
if qtd % 2 == 0:
    print(f"A quantidade de pessoas ({qtd}) é PAR.")
else:
    print(f"A quantidade de pessoas ({qtd}) é ÍMPAR.")