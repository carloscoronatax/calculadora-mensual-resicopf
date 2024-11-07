# Calculadora del ISR mensual de las personas físicas que se encuentran en RESICO

import math

print("¡Bienvenido a la calculadora del ISR mensual de las personas físicas que se encuentran en RESICO!\n Por favor, responda las siguientes preguntas:")

question_1 = float(input("¿Cuál fue su ingreso mensual?: " ))

if question_1 <= 25000:
    impuesto = question_1 * 0.01
    print("El impuesto ISR a pagar antes del dia 17: $", math.ceil(impuesto), "pesos")
elif question_1 > 25000 and question_1 <= 50000:
    impuesto = question_1 * 0.0110
    print('El impuesto ISR a pagar antes del dia 17: $', math.ceil(impuesto), "pesos")
elif question_1 > 50000 and question_1 <= 83333.33:
    impuesto = question_1 * 0.0150
    print('El impuesto ISR a pagar antes del dia 17: $', math.ceil(impuesto), "pesos")
elif question_1 > 83333.33 and question_1 <= 208333.33:
    impuesto = question_1 * 0.02
    print('El impuesto ISR a pagar antes del dia 17: $', math.ceil(impuesto), "pesos")
elif question_1 > 208333.33 and question_1 <= 3500000:
    impuesto = question_1 * 0.0250
    print('El impuesto ISR a pagar antes del dia 17: $',math.ceil(impuesto), "pesos")
else:
    print("Limite de ingreso excedido")

print("¡Gracias por usar la calculadora de impuestos mensual de las personas físicas que se encuentran en RESICO!\n Made by: @carloscoronatax")

# Made by @carloscoronatax