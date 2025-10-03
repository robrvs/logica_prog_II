km = float(input("Digite a quantidade de quilômetros percorridos: "))
oil = float(input("Digite a quantidade de combustível gasto em litros: "))
tot = km * oil
if km > 500:
    print(f"O consumo médio do veículo foi de {tot:.2f} km/l, o que é considerado BOM.")