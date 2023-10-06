# Programación numérica y no numérica

# Nicole Rodriguez DCM-0501
# Ricardo Hernandez DCM-0501
# Santiago Hernandez DCM-0501
# Stefano Parra DCM-0501

# C2x2

from menus import *
from Cal import *
from divisas import *
from perimetro import *
from promedio import *

# Main

while True:
    title()
    mainMenu()
    option = int(input('Selecciona una opcion: '))

    match option:
        case(1):
            print('\nHasta luego\n')
            break
        case(2):
            while True:
                title()
                calcMenu()
                calcOption = int(input('Selecciona una operacion: '))

                match calcOption:
                    case(1):
                        break
                    case(2):
                        title()
                        firstNum = int(input('Ingresa el primer numero: '))
                        secondNum = int(input('Ingresa el segundo numero: '))
                        res = add(firstNum, secondNum)
                        print(f'\nEl resulado es {res}\n')
                    case(3):
                        title()
                        firstNum = int(input('Ingresa el primer numero: '))
                        secondNum = int(input('Ingresa el segundo numero: '))
                        res = subs(firstNum, secondNum)
                        print(f'\nEl resulado es {res}\n')
                    case(4):
                        title()
                        firstNum = int(input('Ingresa el primer numero: '))
                        secondNum = int(input('Ingresa el segundo numero: '))
                        res = mult(firstNum, secondNum)
                        print(f'\nEl resulado es {res}\n')
                    case(5):
                        title()
                        firstNum = int(input('Ingresa el primer numero: '))
                        secondNum = int(input('Ingresa el segundo numero: '))
                        res = int(div(firstNum, secondNum))
                        print(f'\nEl resulado es {res}\n')
                    case(6):
                        title()
                        firstNum = int(input('Ingresa el primer numero: '))
                        secondNum = int(input('Ingresa el segundo numero: '))
                        res = int(mod(firstNum, secondNum))
                        print(f'\nEl resulado es {res}\n')
                    case(_):
                        title()
                        print('Opcion no valida')

        case(3):
            while True:
                title()
                divisasMenu()
                divisasOption = int(input('Selecciona una opcion: '))

                match divisasOption:
                    case(1):
                        break
                    case(2):
                        title()
                        dolarVal = float(input('Ingresa la cantidad de dolares: '))
                        bolivarNum = float(input('Ingresa el valor al cambio en bolivares: '))
                        res = float(dolar_to_bolivar(dolarVal, bolivarNum))
                        print(f'\nLos {dolarVal} dolares son equivalentes a {res} bolivares\n')
                    case(3):
                        title()
                        bolivarNum= float(input('Ingresa la cantidad de bolivares: '))
                        dolarVal = float(input('Ingresa el valor al cambio en dolares: '))
                        res = float(bolivar_to_dolar(bolivarNum, dolarVal))
                        print(f'\nLos {bolivarNum} bolivares son equivalentes a {res} dolares\n')
                    case(_):
                        title()
                        print('Opcion no valida')

        case(4):
            while True:
                title()
                perimetroMenu()
                perimetroOption = int(input('Selecciona una opcion: '))

                match perimetroOption:
                    case(1):
                        break
                    case(2):
                        title()
                        sides = int(input('Ingresa el numero de lados: '))
                        longitud = float(input('Ingresa la longitud de los lados: '))
                        res = float(calcPerimetro(sides, longitud))
                        print(f'\nEl perimetro del poligono de {sides} lados es de {res}\n')
                    case(_):
                        title()
                        print('Opcion no valida')

        case(5):
            while True:
                title()
                promedioMenu()
                promedioOption = int(input('Selecciona una opcion: '))

                match promedioOption:
                    case(1):
                        break
                    case(2):
                        title()
                        nota1 = float(input('Ingresa la primera calificacion: '))
                        nota2 = float(input('Ingresa la segunda calificacion: '))
                        nota3 = float(input('Ingresa la tercera calificacion: '))
                        res = float(calcpromedio(nota1, nota2, nota3))
                        tipo_de_promedio(res)
                    case(_):
                        title()
                        print('Opcion no valida')

        case(_):
            title()
            print('Opcion no valida')