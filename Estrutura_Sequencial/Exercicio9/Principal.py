# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius


fahr = int(input("informe a temperatura em graus Fahrenheit: \n"))

cels = (5 * ( (fahr - 32) / 9))

print(f'{fahr}°F para graus Celcius: {cels:.2f}°C')