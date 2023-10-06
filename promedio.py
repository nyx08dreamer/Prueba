# Programación numérica y no numérica

# Nicole Rodriguez DCM-0501
# Ricardo Hernandez DCM-0501
# Santiago Hernandez DCM-0501
# Stefano Parra DCM-0501

# C2x2

# Funciones de Calculo de Promedio de Notas

def calcpromedio (a, b, c): return (a + b + c) / 3

def tipo_de_promedio (a):
    
    if a == 20:
        print(f'Su promedio de {a} es "Excelente".')
        
    elif a == 19 or a >= 18:
        print(f'Su promedio de {a} es "Muy Bueno".')
        
    elif a == 17 or a >= 15:
        print(f'Su promedio de {a} es "Bueno".')
        
    elif a == 14 or a >= 10:
        print(f'Su promedio de {a} es "Regular".')
        
    elif a == 9 or a >= 0:
        print(f'Su promedio de {a} es "Reprobado".')
        
