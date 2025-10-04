# Raquel Sánchez Guirdo
# 04/10/2025
# Programa que gestiona los clientes de una empresa

nombre_cliente = 'Miguel Hernández'
edad_cliente = 28
saldo_cliente = 2500.75
cliente_activo = True

print( 'Nombre del cliente:', nombre_cliente)
print( 'Edad del cliente:', edad_cliente)
print( 'Saldo del cliente:', saldo_cliente)
print( 'Cliente activo:', 'Sí' if cliente_activo else 'No')

# Calcular el saldo con IVA
IVA = 0.21
saldo_con_IVA = saldo_cliente * (1 + IVA)
print( 'Saldo del cliente con IVA:', saldo_con_IVA)

# Comprobar si el cliente es mayor de edad
if edad_cliente >= 18:
    print( 'El cliente es mayor de edad.')
else:
    print( 'El cliente es menor de edad.')

# Verificar si el cliente está activo y tiene saldo positivo
if cliente_activo and saldo_cliente > 0:
    print( 'El cliente está activo y tiene saldo positivo.')
else:
    print( 'El cliente no está activo o no tiene saldo positivo.')

# Pedir la edad al usuario y convertirla a entero
edad_string = input('Introduce la edad del cliente: ')
edad_cliente = int(edad_string)

# Año de nacimiento del cliente
print( 'Año de nacimiento del cliente:', 2025 - edad_cliente)

# Conversión explícita suma de int y float
print( 'Suma de la edad y el saldo:', edad_cliente + saldo_con_IVA)