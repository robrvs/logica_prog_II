# Solicita o número de horas de exercício por semana
horas_exercicio = int(input("Digite o número de horas que você se exercita por semana: "))

# Verifica em qual plano o usuário se enquadra
if horas_exercicio >= 1 and horas_exercicio <= 3:
    print("Você está no Plano Iniciante!")
elif horas_exercicio >= 4 and horas_exercicio <= 6:
    print("Você está no Plano Intermediário!")
elif horas_exercicio >= 7:
    print("Você está no Plano Avançado!")
else:
    print("Número de horas inválido! Digite um valor igual ou maior que 1.")