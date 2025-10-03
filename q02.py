# Solicita a quantidade de páginas lidas
qtd = int(input("Digite a quantidade de páginas lidas do livro: "))

# Verifica se a quantidade é maior, menor ou igual a 150
if qtd > 150:
    print(f"A quantidade de páginas lidas ({qtd}) é MAIOR que 150.")
elif qtd < 150:
    print(f"A quantidade de páginas lidas ({qtd}) é MENOR que 150.")
else:
    print(f"A quantidade de páginas lidas ({qtd}) é IGUAL a 150.")