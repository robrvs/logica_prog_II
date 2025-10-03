# Solicita a temperatura média do dia
temp = float(input("Digite a temperatura média do dia em graus Celsius: "))

# Verifica se a temperatura está acima ou abaixo de 25 graus
if temp> 25:
    print(f"A temperatura de {temp}°C está QUENTE (acima de 25°C).")
else:
    print(f"A temperatura de {temp}°C está FRIA (abaixo ou igual a 25°C).")