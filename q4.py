# Entrada de dados do usuário
print("=== Calculadora de Viagem ===")
km_percorridos = float(input("Digite a quantidade de quilômetros percorridos: "))
consumo_medio = float(input("Digite o consumo médio do veículo (km/l): "))

# Cálculo do combustível gasto
combustivel_gasto = km_percorridos / consumo_medio

# Verificação se recebe desconto
if km_percorridos > 500:
    recebeu_desconto = "SIM"
else:
    recebeu_desconto = "NÃO"

# Exibição dos resultados
print("\n" + "="*50)
print("RELATÓRIO DA VIAGEM")
print("="*50)
print(f"Distância percorrida: {km_percorridos:.1f} km")
print(f"Combustível consumido: {combustivel_gasto:.2f} litros")
print(f"Recebeu desconto de 10%: {recebeu_desconto}")
print("="*50)

# Mensagem adicional sobre o desconto
if recebeu_desconto == "SIM":
    print("🎉 Parabéns! Você percorreu mais de 500 km e ganhou 10% de desconto!")
else:
    print("💡 Dica: Percorra mais de 500 km na próxima viagem para ganhar desconto!")