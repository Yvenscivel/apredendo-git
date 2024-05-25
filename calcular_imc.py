
def calcularImc():
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    imc = peso/(altura**2)
    if imc < 18.5:
        print(f"Seu IMC é {imc:.2f} e a classificação é Magreza")
    elif imc >= 18.5 and imc <= 24.9:
        print(f"Seu IMC é {imc:.2f} e a classificação é Normal")
    elif imc >= 25.0 and imc <= 29.9:
        print(f"Seu IMC é {imc:.2f} e a classificação é Sobrepeso")
    elif imc >= 30.0 and imc <= 39.9:
        print(f"Seu IMC é {imc:.2f} e a classificação é Obesidade")
    else:
        print(f"Seu IMC é {imc:.2f} e a classificação é Obesidade grave")

calcularImc()
